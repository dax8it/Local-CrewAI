import os
from datetime import datetime
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

load_dotenv()


llm_flash = ChatGoogleGenerativeAI(model="gemini-1.5-flash-exp-0827", temperature=0.5)
llm_llama = ChatOllama(model="llama3.1:70b", base_url="http://localhost:11434")
llm_mistral = ChatOllama(model="mistral-large:latest", base_url="http://localhost:11434")
llm_gemma = ChatOllama(model="gemma2:27b", base_url="http://localhost:11434")
llm_hermes = ChatOllama(model="hermes3:70b", base_url="http://localhost:11434")

# manager_llm = ChatOllama(model="hermes3:70b")
manager_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-exp-0827", temperature=0.5)

# Uncomment the following line to use an example of a custom tool
# from conundrum_crew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

# Uncomment the following line to use an example of a custom tool
# from conundrum.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class ConundrumCrew():
	"""Conundrum crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			llm=llm_mistral,
        	max_iterations=5,
        	max_time=120,
			tools=[search_tool]
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm=llm_hermes,
        	max_iterations=10,
        	max_time=120,	
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			output_file='research.md'
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Conundrum crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			manager_llm=manager_llm,
			process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
			verbose=True,
			# process=Process.sequential,
		)