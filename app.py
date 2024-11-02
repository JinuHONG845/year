import streamlit as st
from datetime import datetime
import random

# 페이지 설정
st.set_page_config(
    page_title="2025년 연하장 생성기",
    page_icon="🎊",
    layout="centered"
)

# CSS 스타일 적용
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
    
    * {
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .handwriting {
        font-family: 'Nanum Pen Script', cursive !important;
        font-size: 24px !important;
        line-height: 1.6 !important;
    }
    
    .title {
        text-align: center !important;
        color: #1E4174 !important;
        font-size: 32px !important;
        margin-bottom: 2rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# 정중한 인사말 목록
formal_greetings = [
    "새해를 맞이하여 귀하와 귀하의 가정에 건강과 행복이 가득하시기를 기원합니다.",
    "2025년 청룡의 해를 맞이하여 소망하시는 모든 일들이 이루어지시길 바랍니다.",
    "새해에도 변함없는 건강과 행운이 함���하시길 진심으로 기원드립니다.",
    "희망찬 2025년, 귀하의 가정에 평안과 축복이 가득하시길 기원합니다."
]

# 캐주얼한 인사말 목록
casual_greetings = [
    "2025년에도 우리 같이 행복하게 지내요! 새해 복 많이 받으세요~ 😊",
    "새해에는 좋은 일만 가득하길! 올해도 잘 부탁해요~ 🎊",
    "해피 뉴이어! 2025년에도 우리 우정 변치 말아요~ ⭐",
    "새해에는 하시는 모든 일이 대박나시길! 화이팅! 🎉"
]

# 배경 이미지 CSS 추가
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&family=Gaegu&family=Poor+Story&family=Single+Day&display=swap');
    
    .letter-container {
        background-image: url('https://img.freepik.com/free-photo/crumpled-paper-background_1373-431.jpg');
        background-size: cover;
        padding: 40px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .handwriting {
        font-family: var(--font-family) !important;
        font-size: 24px !important;
        line-height: 1.8 !important;
        color: #333 !important;
    }
    
    .title {
        text-align: center !important;
        color: #1E4174 !important;
        font-size: 32px !important;
        margin-bottom: 2rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# 폰트 리스트
fonts = ['Nanum Pen Script', 'Gaegu', 'Poor Story', 'Single Day']

st.markdown("<h1 class='title'>✨ 2025년 연하장 생성기 ✨</h1>", unsafe_allow_html=True)

# 입력 폼
name = st.text_input("받는 분의 이름을 입력해주세요")
style = st.radio("연하장 스타일을 선택해주세요", ["정중하게", "캐주얼하게"])

if st.button("연하장 생성하기"):
    if name:
        st.markdown("---")
        
        # 랜덤 폰트 선택
        random_font = random.choice(fonts)
        
        # 현재 날짜
        current_date = datetime.now().strftime("%Y년 %m월 %d일")
        
        # 스타일에 따른 인사말 선택
        greeting = random.choice(formal_greetings) if style == "정중하게" else random.choice(casual_greetings)
        
        # 연하장 내용 생성 (편지지 배경 포함)
        message = f"""
        <div class="letter-container">
            <div class="handwriting" style="font-family: {random_font} !important;">
                {name}님께,<br><br>
                {greeting}<br><br>
                {current_date}
            </div>
        </div>
        """
        
        st.markdown(message, unsafe_allow_html=True)
    else:
        st.error("이름을 입력해주세요!")