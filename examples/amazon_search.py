"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

from lumivor import Agent
from langchain_openai import ChatOpenAI
import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
    task='Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result',
    llm=llm,
)


async def main():
    await agent.run(max_steps=3)
    agent.create_history_gif()


asyncio.run(main())
