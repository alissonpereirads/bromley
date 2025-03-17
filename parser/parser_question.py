from langchain.output_parsers import PydanticOutputParser
from model.question import QuestionCategory

# Criando um Output Parser para processar a resposta do LLM
output_parser = PydanticOutputParser(pydantic_object=QuestionCategory)
