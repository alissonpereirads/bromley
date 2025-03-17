from langchain.prompts import ChatPromptTemplate


def question_prompt():
    return ChatPromptTemplate.from_template(
        """
        Classifique a seguinte reclamação, solicitação ou comentário do usuário em uma das categorias:
        - 'Dúvida Técnica' → Se for uma pergunta relacionada a problemas técnicos, como funcionamento de dispositivos, software, etc.
        - 'Sugestão' → Se for uma sugestão de melhoria ou ideia para um produto ou serviço.
        - 'Reclamação' → Se for uma reclamação sobre um produto, serviço ou atendimento.
        - 'Outro' → Se não se encaixar em nenhuma das categorias acima.

        Por favor, retorne a categoria e a pergunta original em formato JSON.

        Pergunta: {pergunta}
        """
    )
