import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


#set OPENAI_API_KEY has been set up environment variables
async def main():

    model_client = OpenAIChatCompletionClient(model="gpt-4o")

    # create Researcher agent
    researcheragent = AssistantAgent(name="ResearcherAgent", model_client=model_client,
                                     system_message="You are a researcher. your role is to gather information and provide research findings only."
                                     "Do not write articles or crate content, just provide research data and facts.")

    # Writer agent
    writeragent = AssistantAgent(name="WriterAgent", model_client=model_client,
                                     system_message="You are a writer. Your role is to take research information and Create well written articles."
                                                    "wait for research to be provided, then write the content")
    # Critic agent
    criticagent = AssistantAgent(name="CriticAgent", model_client=model_client,
                                 system_message="You are a critic. Review written content and provide feedback."
                                                "Say 'TERMINATE' when satisfied with the final result.")

    text_termination = TextMentionTermination("TERMINATE")

    max_messages_termination = MaxMessageTermination(max_messages=5)

    termination = text_termination | max_messages_termination

    team = SelectorGroupChat(participants=[criticagent, writeragent, researcheragent],
                             model_client=model_client, termination_condition=termination,
                             allow_repeated_speaker=True)

    await Console(team.run_stream(
        task="Research renewable energy trends and write a brief article about the future of solar power."))

asyncio.run(main())