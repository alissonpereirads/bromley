from langchain.schema.runnable import RunnablePassthrough
from parser.parser_question import output_parser
from prompt.prompt_question import question_prompt
from config.config_question import carregar_modelo


# Criando o pipeline com LCEL
def chain_q():

    prompt = question_prompt()
    llm = carregar_modelo()
    parser = output_parser
    pipeline = (
        prompt
        | llm
        | RunnablePassthrough()  # Passa a saída do LLM sem modificar
        | parser
    )

    return pipeline
