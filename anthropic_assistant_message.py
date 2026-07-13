import anthropic

client = anthropic.Anchropic()

# 대화 기록을 저장할 리스트
conversation = []

# 사용자 입력 추가
conversation.append({"role":"user", "content":"안녕하세요"})

# 클로드 호출
response = client.message.create(
    model="claude-3-5-haiku-latest", # 모델 선택
    max_tokens=1000, # 최대 토큰
    messages=conversation
)

# 응답 출력 및 대화 기록에 추가
asssistant_message = response.content[0].text
print(asssistant_message)
conversation.append({"role":"asssistant", "content":asssistant_message})

# 다음 사용자 입력
conversation.append({"role":"user", "content":"다시 한번 더 설명해"})

# 다시 클로드 호출
response = client.message.create(
    model="claude-3-5-haiku-latest",
    max_tokens=1000,
    messages=conversation
)

# 두 번째 응답 출력
print(response.content[0].text)