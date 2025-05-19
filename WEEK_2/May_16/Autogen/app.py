import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console  # If you want to use Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
import os
from dotenv import load_dotenv

load_dotenv()



async def main():
    model_client = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        api_key=os.getenv("API_KEY")
    )

    assistant = AssistantAgent(
        name="assistant",
        model_client=model_client,
    )

    termination = TextMentionTermination("TERMINATE")

    # If Console supports single agent usage without GroupChat
    group_chat = RoundRobinGroupChat([assistant],termination_condition=termination)


    # Run the conversation/task
    await Console(group_chat.run_stream(task="Is the earth flat?"))

    await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())
