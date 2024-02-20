# main.py
from flask import Flask
from crewai import Crew, Process
from tasks import tarefa_pesquisa, tarefa_escrita

app = Flask(__name__)

@app.route('/')
def execute_crew():
    # Formando a equipe focada em tecnologia
    equipe = Crew(
      agents=[tarefa_pesquisa.agent, tarefa_escrita.agent],
      tasks=[tarefa_pesquisa, tarefa_escrita],
      process=Process.sequential  # Execução sequencial das tarefas
    )

    # Iniciando o processo de execução das tarefas
    resultado = equipe.kickoff()
    return {"resultado": resultado}

if __name__ == '__main__':
    app.run(debug=True)
