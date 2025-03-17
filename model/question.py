from pydantic import BaseModel, Field


# Definição da estrutura de saída
class QuestionCategory(BaseModel):
    """Modelo que classifica perguntas em categorias predefinidas."""

    categoria: str = Field(
        description="Categoria da pergunta ('Dúvida Técnica', 'Sugestão', 'Reclamação' ou 'Outro')"
    )

    pergunta: str = Field(description="Pergunta a ser classificada")
