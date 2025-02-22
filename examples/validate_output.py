"""
Demostrate output validator.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

from lumivor import ActionResult, Agent, Controller
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


load_dotenv()

controller = Controller()


class DoneResult(BaseModel):
    title: str
    comments: str
    hours_since_start: int


# we overwrite done() in this example to demonstrate the validator
@controller.registry.action('Done with task', param_model=DoneResult)
async def done(params: DoneResult):
    result = ActionResult(
        is_done=True, extracted_content=params.model_dump_json())
    print(result)
    # NOTE: this is clearly wrong - to demonstrate the validator
    # return result
    return 'blablabla'


async def main():
    task = 'Go to hackernews hn and give me the top 1 post'
    model = ChatOpenAI(model='gpt-4o')
    agent = Agent(task=task, llm=model,
                  controller=controller, validate_output=True)
    # NOTE: this should fail to demonstrate the validator
    await agent.run(max_steps=5)


if __name__ == '__main__':
    asyncio.run(main())
