"""
    엔트로픽 API는 stream 메서드를 별도로 제공하고 with를 사용한 컨텍스트 메니저 기능도 제공한다.
"""

import anthropic
import rich

client = anthropic.Anchropic()

"""
    with 구문을 사용하면 __enter__, __exit__ 메서드를 통해 스트림 객체의 생성과 종료를 자동으로 관리할 수 있다.
    client.message.stream.create()는 컨텍스트 매니저를 지원하는 객체를 반환하며, 이를 통해 스트리밍 응답을 더 안전하고 간편하게 처리
    엔트로픽은 max_token을 지정해줘야함.
"""
prompt = "한국의 수도는 어디인가요?"
with client.message.stream.create( # 컨텍스트 매니저를 사용한 스트리밍 세션
    max_tokens=1024,
    messages=[{"role":"user", "content":prompt}],
    model="claude-3-5-haiku-latest",
) as stream:
    for event in stream: # 스트리밍 중 일때
        if event.type == "text": # 텍스트 타입 이벤트만 처리
            print(event.text, end="")

    print()

    # 최종 응답 출력
    rich.print(stream.get_final_message())