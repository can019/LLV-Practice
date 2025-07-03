print("LangChain 테스트 시작")

# ✅ os 모듈: 운영체제와의 상호작용(환경변수 등)을 위해 사용
import os

# ✅ dotenv에서 load_dotenv: .env 파일을 읽어 환경변수로 등록하는 함수
from dotenv import load_dotenv

# ✅ .env 파일을 찾아서 환경변수를 불러옴 (예: OPENAI_API_KEY)
load_dotenv()

# ✅ LangChain OpenAI LLM 클래스 최신 공식 import 방법
# (langchain 0.1 이후부터는 별도 패키지에서 가져와야 함)
from langchain_openai import OpenAI

# ✅ OpenAI LLM 객체 생성
# temperature=0: 일관적이고 정답에 가까운 응답을 유도 (창의성 낮춤)
# api_key: 환경변수로 자동 불러옴, 따로 지정안하면 OPENAI_API_KEY를 자동인식
llm = OpenAI(
    temperature=0
)

# ✅ LLM에 프롬프트(질문) 입력하여 답변받기
response = llm("")

# ✅ 응답 출력
print(response)
