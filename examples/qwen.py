import asyncio
import os

from langchain_ollama import ChatOllama

from lumivor import Agent


async def run_search():
    agent = Agent(
        task=(
            '1. Go to https://www.reddit.com/r/LocalLLaMA'
            "2. Search for 'lumivor labs' in the search bar"
            '3. Click search'
            '4. Call done'
        ),
        llm=ChatOllama(
            # model='qwen2.5:32b-instruct-q4_K_M',
            # model='qwen2.5:14b',
            model='qwen2.5:latest',
            num_ctx=128000,
        ),
        max_actions_per_step=1,
        tool_call_in_content=False,
    )

    await agent.run()


if __name__ == '__main__':
    asyncio.run(run_search())
