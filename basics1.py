import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def main():
    print("hello world, I am inside the function!")

    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        # api_key="sk-...", # Optional if you have an OPENAI_API_KEY environment variable set.
    )

    assistant = AssistantAgent(name="assistant",model_client=openai_model_client)
    await Console(assistant.run_stream(task="What is 25 * 8?"))
    await openai_model_client.close()


asyncio.run(main())