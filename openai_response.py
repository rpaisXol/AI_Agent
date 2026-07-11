from openai import OpenAI

# OpenAI 클라이언트 생성
client = OpenAI(api_key="sk-...")

# OpenAI 챗 컴플리션 API를 사용하여 AI의 응답을 받는 함수
"""
    reponse.create() 함수는 입력된 프롬프트로 AI 응답을 받아오는 함수이다.
    원래는 파라미터가 더 많지만 우선 model, tools, input 3개만 사용,
    model은 말 그대로 모델명이고, input은 프롬프트이다.
    결과값에서 output_text속성에는 텍스트로 응답이 있다.
    ChatGPT에서 하던 대로 웹을 검색해서 알려준다.
    tools: LLM이 사용할 수 있는 도구를 리스트로 정의, web_search_preview 도구를 사용하면, 기본 내장된 웹 검색 도구를 사용
"""

def get_reponses(prompt, model="gpt-5-mini"):
    # 챗 컴플리션 API 호출
    response = client.responses.create(
        model=model, # 사용할 모델 지정
        tools=[{"type": "web_search_preview"}], # 웹 검색 도구 활성화
        input=prompt # 사용자 입력 전달
    )

    return response.output_text # 텍스트 응답만 반환

# 사용자 입력을 받아 AI의 응답 출력
if __name__ == "__main__":
    prompt = """https://platform.openai.com/docs/guides/gpt-best-practices에 대해 요약 정리좀 부탁해"""
    output = get_reponses(prompt)
    print(f"ChatGPT: {output}")