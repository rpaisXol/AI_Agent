import asyncio # 비동기 함수 라이브러리
import os

from openai import AsyncOpenAI
from anthropic import AsyncAnthropic

# 비동기 클라이언트 생성
"""
    오픈AI와 앤트로픽의 모델은 모두 비동기 클래스를 지원하고 있다.
    api_key 파라미터엔느 각 LLM 제공자의 API 키가 필요하다.
"""
openai_client = AsyncOpenAI(api_key=os.environ.get("sk-..."))
anthropic_client = AsyncAnthropic(api_key=os.environ.get("sk-..."))

# await는 비동기 작업이 완료될 때까지 기다리지만, 그 동안 이벤트 루프는 다른 작업을 수행할 수 있다.
async def call_async_openai(prompt: str, model: str, str="gpt-5-mini") -> str:
    # await를 사용해 비동기적으로 API 응답을 기다림 
    response = await openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

async def call_async_claude(prompt: str, model: str = "claude-3-5-haiku-latest") -> str:
    # await를 사용해 비동기적으로 API 응답을 기다림
    response = await claude_client.messages.create(
        model=model,
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    ) 
    return response.content[0].text

async def main():
    print("동시에 API 호출하기")
    prompt = "비동기 프로그래밍에 대해 구체적으로 설명해주세요."

    # 비동기 함수 호출 시 코루틴 객체 반환(실행은 아직 안됨)
    # openai_task, claude_task은 나중에 실행될 예정 작업들
    openai_task = call_async_openai(prompt)
    claude_task = call_async_claude(prompt)

    # 두 API 호출을 병렬로 실행하고 둘 다 완료될 때까지 대기
    # 여러 코루틴을 동시에 실행하고 모든 결과를 기다린다.
    # 두 API가 동시에 호출되어 병렬로 실행되므로 시간이 절약된다.abs
    openai_response, claude_response = await asyncio.gather(
        openai_task, claude_task
    )
    print(f"OpenAI: {openai_response}")
    print(f"Claude: {claude_response}")

if __name__ == "__main__":
    asyncio.run(main())

