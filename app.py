from fastapi import FastAPI
from AdImages import AdImage
from fastapi.middleware.cors import CORSMiddleware
import replicate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/')
def ad_image(business: str, brand_name: str):
    ad = AdImage()
    image_prompt = ad.my_chain.run({"business": business, "brand_name": brand_name})
    image = replicate.run(
        "stability-ai/sdxl:c221b2b8ef527988fb59bf24a8b97c4561f1c671f73bd389f866bfb27c061316",
        input={
            "prompt": image_prompt}
    )
    return {
        'ad image': image
    }
