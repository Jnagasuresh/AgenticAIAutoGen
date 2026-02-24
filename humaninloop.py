import asyncio
import os

from autogen_agentchat.agents import UserProxyAgent, AssistantAgent
from autogen_agentchat.base import TerminationCondition
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

#os.environ["OPENAI_API_KEY"] = "abc"

async def main():
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o")
    mathsassistant = AssistantAgent(name="MathsAssistant", model_client=openai_model_client,
                                    system_message="You are helpful math tutor. Help the user to solve math problems step by step"
                                    "When the user says 'Thanks Done' or similar, acknowledge and say 'Lesson Complete' to end session")

    user_proxy = UserProxyAgent(name="Student")

    team = RoundRobinGroupChat(participants=[user_proxy, mathsassistant],
                               termination_condition=TextMentionTermination("Lesson Complete"))

    await Console(team.run_stream(task="I need help with algebra problem"))

asyncio.run(main())
