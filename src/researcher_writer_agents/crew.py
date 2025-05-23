from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class ResearcherWriterAgents():
    """ResearcherWriterAgents crew"""

    ollama_mistral = LLM(
        model='ollama/mistral:latest',
        base_url='http://localhost:11434',
        # temperature=0.2,
        # max_tokens=2000,
        # top_p=0.9,
        # top_k=40,
        # n=1,
        # stop=['\n\n'],
    )

    # agents: List[BaseAgent]
    # tasks: List[Task]

    @agent
    def planner(self) -> Agent:
        return Agent(
            config=self.agents_config['planner'], 
            verbose=True,
            allow_delegation=False,
            llm=self.ollama_mistral,
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True,
            allow_delegation=False,
            llm=self.ollama_mistral,
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'], 
            verbose=True,
            allow_delegation=False,
            llm=self.ollama_mistral,
        )



    @task
    def plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_task'],
        )

    @task
    def write_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_task'],
            # output_file='report.md'
        )

    @task
    def edit_task(self) -> Task:
        return Task(
            config=self.tasks_config['edit_task'],
            output_file='outputs/article.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResearcherWriterAgents crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
