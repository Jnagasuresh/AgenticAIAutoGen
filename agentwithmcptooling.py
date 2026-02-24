import asyncio
import os

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench

# set OPENAI_API_KEY environment variable
async def main():
    filesystem_server_params = StdioServerParams(command="npx",
                                                 args=[
                                                     "-y",
                                                     "@modelcontextprotocol/server-filesystem",
                                                     r"C:\src\pyprojects\AgenticAIAutoGen"],
                                                 read_timeout_seconds=60
                                                 )

    fs_workbench = McpWorkbench(filesystem_server_params)

    async with fs_workbench as fs_wb:
        model_client = OpenAIChatCompletionClient(model="gpt-4o")

        # Maths Tutor agent
        math_tutor = AssistantAgent(name="MathTutor", model_client=model_client, workbench=fs_wb,
                                    system_message="You are a helpful and patient Math Tutor. Your goal is to guide the user through mathematical problems by providing clear, "
                                                   "step-by-step explanations You have to access file system"
                                                   "When the user says 'THANKS DONE' or similar, acknowledge and say "
                                                   "'LESSON COMPLETE' to end session.")
        # student (User)
        user_proxy = UserProxyAgent(name="Student")

        teamup = RoundRobinGroupChat(participants=[user_proxy, math_tutor],
                                     termination_condition=TextMentionTermination("LESSON COMPLETE"))

        await Console(teamup.run_stream(task="I need help with algebra problem. Tutor, feel free to create files to help with student learning."))

        await model_client.close()


asyncio.run(main())