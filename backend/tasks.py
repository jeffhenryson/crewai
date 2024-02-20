# tasks.py
from crewai import Task
from langchain_community.tools import DuckDuckGoSearchRun
from agents import pesquisador, escritor, tema

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
