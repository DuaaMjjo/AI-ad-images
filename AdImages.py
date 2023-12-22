from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()


class AdImage:
    llm = ChatOpenAI(
        temperature=0,
        model_name='gpt-3.5-turbo'
    )

    image_generation_template = """I want you to write prompt for image generation to make it generate advertisement 
    image for my {business} my brand name '{brand_name}' Return the prompt."""

    prompt_template = PromptTemplate(
        input_variables=["business", "brand_name"],
        template=image_generation_template,
    )
    my_chain = LLMChain(llm=llm, prompt=prompt_template)
