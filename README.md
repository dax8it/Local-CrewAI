# Conundrum Crew

Welcome to the Conundrum Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/conundrum/config/agents.yaml` to define your agents
- Modify `src/conundrum/config/tasks.yaml` to define your tasks
- Modify `src/conundrum/crew.py` to add your own logic, tools and specific args
- Modify `src/conundrum/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
or
```bash
poetry run conundrum
```

This command initializes the conundrum Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The conundrum Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Conundrum Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

---
# Actual installation process for this crew.

# Installing this specific crew.

Follow These Steps if using Anaconda env:

1. Create Anaconda environment (myenv is the name of your environment)
    ```bash
    conda create --name myenv python=3.12
    ```

2. Activate your conda env
    ```bash
    conda activate myenv
    ```

3. Install Crewai and tools
    ```bash
    pip install "crewai[tools]"
    ```

4. Create a crew (replace crew_name)
    ```bash
    crewai create crew crew_name
    ``` 
    
5. Go to that newly created directory > make sure your conda env is active
    ```bash
    conda activate environment myenv
    ```

5. Open VScode go to directory

6. Use .env file for API keys (copy keys into the env file for openai, serper,g google) install the env
    ```bash
    pip install python-dotenv
    ```

7. Langchain install: For ollama local models 
    ```bash
    pip install langchain_ollama
    ```

8. Install google gemini to use in project
    ```bash
    pip install langchain_google_genai
    ```

9. Install all the dependencies
    ```bash
    poetry install
    ```

10. Start crew
    ```bash
    crewai run
    ```

11. Enter topic

Note: In order to allow for user input to run the crew, we added code to main.py
def get_user_topic():
    """Prompt the user to enter a topic."""
    return input("Please enter a topic for today's post: ")

 topic = get_user_topic()

    inputs = {
        'topic': topic
    }





