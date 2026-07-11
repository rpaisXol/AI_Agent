import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 파일에서 환경 변수 로드
load_dotenv()

# OpenAI 클라이언트 생성, API 키로 OpenAI 클라이언트를 초기화
client = OpenAI(api_key="sk-...")

# OpenAI 챗 컴플리션 API를 사용하여 AI의 응답을 받는 함수
def get_chat_completion(prompt, model="gpt-5-mini"):
    # 챗 컴플리션 API 호출
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "당신은 친절하고 도움이 되는 AI 비서입니다."},
            {"role": "user", "content": prompt}
        ]
    )
    # API 응답에서 텍스트 내용을 추출하여 반환, 실제 서비스 코드에선 try except문을 사용해서 예외처리 진행
    return response.choices[0].message.content


# 사용자 입력을 받아 AI의 응답 출력
if __name__ == "__main__":
    user_input = input("AI에게 물어볼 질문을 입력하세요.: ")
    ai_response = get_chat_completion(user_input)
    print(f"ChatGPT: {ai_response}")