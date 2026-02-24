import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
#OPENAI_API_KEY has been set up environment variables

async def main():
    # Create First agent
    model_client = OpenAIChatCompletionClient(model="gpt-40")

    mathTeacherAgent = AssistantAgent(name="MathTeacher", model_client=model_client, system_message="You are a math teacher, Explain concepts clearly and ask follow-up questions")

    studentAgent = AssistantAgent(name="Student", model_client=model_client, system_message="You are a curious student, Ask questions and show your thinking process")
    team = RoundRobinGroupChat(participants=[mathTeacherAgent, studentAgent], termination_condition=MaxMessageTermination(max_messages=6))

    await Console(team.run_stream(task="Let's discuss what is multiplication and how it works"))
    await model_client.close()


asyncio.run(main())
