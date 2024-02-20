from langchain_community.tools import DuckDuckGoSearchRun

from dotenv import load_dotenv

from crewai import Crew, Process
from crewai import Agent
from crewai import Task

import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

tema = 'IA na saúde'

# Criando um agente pesquisador sênior
pesquisador = Agent(
  role='Filósofo Contemporâneo',
  goal=f'Descobrir tecnologias revolucionárias sobre {tema}',
  verbose=True,
  backstory="""Movido pela curiosidade, você está na vanguarda da
  inovação, ansioso para explorar e compartilhar conhecimentos que poderiam mudar
  o mundo."""
)

# Criando um agente escritor
escritor = Agent(
  role='Escritor',
  goal=f'Narrar histórias tecnológicas envolventes sobre {tema}',
  verbose=True,
  backstory="""Com um talento para simplificar temas complexos, você cria
  narrativas envolventes que cativam e educam, trazendo novas
  descobertas à luz de uma maneira acessível."""
)

ferramenta_pesquisa = DuckDuckGoSearchRun()

# Tarefa de pesquisa para identificar tendências de IA
tarefa_pesquisa = Task(
  description=f"""Identifique a próxima grande tendência em {tema}.
  Foque em identificar prós e contras e a narrativa geral.

  Seu relatório final deve articular claramente os pontos-chave,
  suas oportunidades de mercado e riscos potenciais.
  """,
  expected_output='Um relatório compreensivo de 3 parágrafos sobre as últimas tendências de IA.',
  max_inter=3,
  tools=[ferramenta_pesquisa],
  agent=pesquisador
)

# Tarefa de escrita baseada nas descobertas da pesquisa
tarefa_escrita = Task(
  description=f"""Componha um artigo perspicaz sobre {tema}.
  Foque nas últimas tendências e como isso está impactando a indústria.
  Este artigo deve ser fácil de entender, envolvente e positivo.
  """,
  expected_output=f'Um artigo de 4 parágrafos sobre os avanços de {tema}.',
  tools=[ferramenta_pesquisa],
  agent=escritor
)

# Formando a equipe focada em tecnologia
equipe = Crew(
  agents=[pesquisador, escritor],
  tasks=[tarefa_pesquisa, tarefa_escrita],
  process=Process.sequential  # Execução sequencial das tarefas
)

# Iniciando o processo de execução das tarefas
resultado = equipe.kickoff()
print("resultado: ", resultado)
