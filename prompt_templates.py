from langchain.prompts import ChatPromptTemplate

welcome_user_prompt = ChatPromptTemplate.from_template(
    """
YOU ARE A GREETER of the WHATZIT AI ( a random data generator AI system ), 
who has only one job to greet user and define your purpose.
"""
)

random_generation_prompt = ChatPromptTemplate.from_template(
    """
YOU ARE A RANDOM DATA GENERATOR, 
you need to generate the list of N number of objects of a particular CATEGORY.

So generate a json list of {num} objects of {category}, each object having properties:
 
 - id: a unique id (uuid v4)
 - name: name of the item
 - description: a short description of the item
"""
)
