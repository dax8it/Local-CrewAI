import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_community.llms import OpenAI, Ollama
from dotenv import load_dotenv
import litellm
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

load_dotenv()
litellm.api_key = os.getenv('GOOGLE_API_KEY')
# Set the Google API key for LiteLLM to use Gemini LLM Models

# os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY') 

# Uncomment the following line to use an example of a custom tool
# from conundrum_crew.tools.custom_tool import MyCustomTool
 



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
			llm='ollama/hermes3:latest',
        	max_iterations=5,
        	max_time=120,
			tools=[search_tool]
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm='ollama/gemma2:27b',
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
			manager_llm='gemini/gemini-1.5-flash-exp-0827', 
			process=Process.hierarchical,
			# process=Process.sequential,
			verbose=True,
		)
