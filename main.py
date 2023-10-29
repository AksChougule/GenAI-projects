from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import Constants

def generate_pet_name(user_animal_type, pet_color):
    llm = OpenAI(temperature=0.7, openai_api_key=Constants.OPENAI_API_KEY)

    prompt_template_name = PromptTemplate(
        input_variables=['user_animal_name','pet_color'],
        template = "I have a {user_animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet"
    )
    
    name_chain = LLMChain(llm=llm, prompt = prompt_template_name)

    response = name_chain({'user_animal_type':user_animal_type, 'pet_color':pet_color})
    
    return response

if __name__ == "__main__":
    print(generate_pet_name("cat","white"))
