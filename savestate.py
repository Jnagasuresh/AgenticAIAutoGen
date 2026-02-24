import asyncio
import json
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

#OPENAI_API_KEY has been set up environment variables

# this snippet to show how the agent context is saved for later use.
async def main():
    #create first assitant agent
    model_client = OpenAIChatCompletionClient( model="gpt-4o" )
    mainagent = AssistantAgent( name="Helper", model_client=model_client)

    backupagent = AssistantAgent(name="BackupHelper", model_client=model_client)
    state = await mainagent.save_state()
    # Save state to physcial file
    with open("memory.json","w") as f:
        json.dump(state,f, default=str)

    # Read the physical file to state
    with open("memory.json","r") as f:
        saved_state = json.load(f)

    await backupagent.load_state(saved_state)
    await Console(backupagent.run_stream(task="what is my favourite color"))

    await model_client.close()



asyncio.run(main())