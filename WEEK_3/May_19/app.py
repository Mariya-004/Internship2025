import asyncio
from selenium import webdriver
from bs4 import BeautifulSoup
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
driver = webdriver.Chrome(options=options)

# Tool to fetch page content

async def fetch_page(url: str) -> str:
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, driver.get, url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    main_content = soup.find('div', id='mw-content-text')
    if main_content:
        # Extract only paragraphs, headings, and list items
        elements = main_content.select('p, h2, h3, li')
        text = '\n'.join(el.get_text(strip=True) for el in elements if el.get_text(strip=True))
        return text
    else:
        return soup.get_text(separator='\n', strip=True)


# Main async function
async def main():
    model_client = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",  # Replace with your actual model
        api_key=os.getenv("API_KEY")
    )

    # Define the researcher agent
    researcher = AssistantAgent(
        name="Researcher",
        description="An agent that searches the web for relevant content.",
        model_client=model_client,
        system_message="You are a researcher agent. You can use the 'fetch_page' tool to fetch content from Google based on the user's query and return the text in a neat way. Pass the results to the Summarizer.",
        tools=[fetch_page],
    )

   

    # Define the summarizer agent
    textSummarizer = AssistantAgent(
        name="TextSummarizer",
        description="An agent that summarizes web content into concise points.",
        model_client=model_client,
        system_message="You are an assistant that summarizes the provided web content into concise points (under 200 words)."
    )
    # Define the user agent
    user= UserProxyAgent(
        name='User',
        description='A user agent that interacts with the agents',
    )
    #create a group chat
    termination=TextMentionTermination("TERMINATE")
    group_chat = RoundRobinGroupChat(
        [researcher, textSummarizer, user],
        termination_condition=termination,
    )

    # Use the researcher agent to fetch content
    url = "https://en.wikipedia.org/wiki/Dora_the_Explorer"
    
    await Console(group_chat.run_stream(task=url))
    
    
   

if __name__ == "__main__":
    asyncio.run(main())