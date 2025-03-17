# Classificador de Reclamações e Solicitações com LLM

Bem-vindo ao meu projeto de estudo sobre Large Language Models (LLMs) e suas aplicações práticas! Este é um classificador de reclamações, solicitações e comentários de usuários, desenvolvido como parte do meu aprendizado em Ciência de Dados e Inteligência Artificial.

Como estudante do 3º semestre de Ciência de Dados, tenho me dedicado a explorar ferramentas e frameworks modernos para criar soluções inteligentes e funcionais. Este projeto é um exemplo do meu esforço em aprender e aplicar conceitos de IA, especialmente no uso de LLMs para automação e classificação de textos.

## Sobre o Projeto

Este projeto é um classificador automático que utiliza um modelo de linguagem (LLM) para analisar reclamações, solicitações ou comentários de usuários e direcioná-los para o departamento correto. Ele foi desenvolvido com o objetivo de estudar e praticar o uso de ferramentas como LangChain, Streamlit e modelos de linguagem da Groq.

A aplicação é capaz de classificar entradas em quatro categorias principais:

- **Dúvida Técnica**
- **Sugestão**
- **Reclamação**
- **Outro**

Além de ser um exercício técnico, este projeto também serve como uma demonstração do meu interesse em resolver problemas reais usando IA e Machine Learning.

## Ferramentas e Tecnologias Utilizadas

Aqui estão as principais ferramentas e frameworks que utilizei para desenvolver este projeto:

- **LangChain**: Para criar pipelines de processamento de linguagem natural (NLP) e integrar o modelo de linguagem.
- **Groq (LLM)**: Utilizei o modelo llama-3.3-70b-versatile da Groq para realizar a classificação das entradas.
- **Streamlit**: Para criar uma interface simples e interativa, permitindo que usuários testem o classificador.
- **Pydantic**: Para validação e estruturação dos dados de saída.


## Como Funciona?

1. O usuário insere uma reclamação, solicitação ou comentário na interface do Streamlit.
2. O texto é processado pelo modelo de linguagem (LLM), que o classifica em uma das categorias pré-definidas.
3. O resultado é exibido na interface, mostrando a categoria e a pergunta original em formato JSON.

## Como Executar o Projeto

Se você quiser testar o projeto localmente, siga os passos abaixo:

### Pré-requisitos

- Python 3.8 ou superior
- Conta na Groq para obter uma API key

### Passos para Execução

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` na raiz do projeto e adicione sua API key da Groq:
```plaintext
GROQ_API_KEY=sua_chave_aqui
```

4. Execute a aplicação com o Streamlit:
```bash
streamlit run main.py
```

5. Acesse a interface no seu navegador e teste o classificador!

## Exemplos de Entradas

Aqui estão alguns exemplos de entradas que você pode testar:

- **Dúvida Técnica**: "Meu celular não está carregando, mesmo quando conecto o carregador. O que pode ser?"
- **Sugestão**: "Seria ótimo se vocês adicionassem um modo escuro ao aplicativo."
- **Reclamação**: "Comprei um produto que veio com defeito e não consigo trocar."
- **Outro**: "Qual é o horário de funcionamento da loja?"

## Objetivo do Projeto

Este projeto foi desenvolvido como parte do meu estudo em Ciência de Dados e Inteligência Artificial. Meu objetivo é explorar ferramentas modernas e frameworks de IA para criar soluções práticas e funcionais. Além disso, busco aplicar conceitos teóricos em projetos reais, como este, para consolidar meu aprendizado e demonstrar minhas habilidades.

## 📚 Aprendizados
Ja tenho um projeto que se assemelha bastante com este o [Girafales](https://github.com/alissonpereirads/girafales), porem na busca por consolidar fundamentos a repetição é a mãe do aprendizado.

Este projeto me permitiu:

- Consoliadar meu conhecimento em LLMs e suas aplicações.
- Repetir o trabalho com APIs e frameworks modernos como LangChain e Streamlit.
- Treinar engenharia de prompt e processamento de linguagem natural.
- Exercitar minha capacidade de documentar e compartilhar projetos no GitHub.
- Estudar Output parsers


## Sobre Mim

Olá! Meu nome é Alisson Pereira, sou estudante de Ciência de Dados no 3º semestre e um entusiasta de Inteligência Artificial e Machine Learning. Estou em busca da minha primeira oportunidade de estágio para aplicar meus conhecimentos em projetos reais e continuar aprendendo.

Se você gostou deste projeto ou tem alguma sugestão, sinta-se à vontade para entrar em contato comigo! Você pode me encontrar no:

- **LinkedIn**: [Alisson Pereira](https://www.linkedin.com/in/alisson-pereira-ds/)
- **E-mail**: alissonpereira.contato@gmail.com
- **GitHub**: [alissonpereirads](https://github.com/alissonpereirads)

---

Feito com ❤️ por [Alisson Pereira].
*Estudante de Ciência de Dados | Apaixonado por IA e Aprendizado Contínuo*
