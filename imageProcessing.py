import asyncio
import os


from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient



async def main():
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o")

    assistant = AssistantAgent(name="MultiModalAssistant", model_client=openai_model_client)

    image = Image.from_file("assets/samplepic.png")

    multi_model_message = MultiModalMessage(
        content=["what do you see in this image", image], source="user"
    )
    await Console(assistant.run_stream(task=multi_model_message))
    await openai_model_client.close()


asyncio.run(main())