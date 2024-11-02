import streamlit as st
from datetime import datetime
import random

# 페이지 설정
st.set_page_config(page_title="연하장 생성기", layout="centered")

# 인사말 리스트
formal_greetings = [
    "새해에도 변함없는 건강과 행운이 함께하시길 진심으로 기원드립니다.",
    "희망찬 새해, 늘 건강과 행복이 가득하시길 기원드립니다.",
    "새해에도 좋은 일만 가득하시고 복 많이 받으시길 바랍니다."
]

casual_greetings = [
    "새해에도 변함없는 건강과 행운이 함께하길 바라!",
    "올해도 우리 같이 힘내보자! 새해 복 많이 받아~",
    "새해에는 좋은 일만 가득하길! 항상 응원할게!"
]

# CSS 스타일
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&family=Gaegu&family=Hi+Melody&family=Dongle&family=Gamja+Flower&family=East+Sea+Dokdo&display=swap');
    
    .letter-container {
        background-image: url('https://img.freepik.com/free-photo/crumpled-paper-background_1373-431.jpg');
        background-size: cover;
        padding: 40px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.title("🎊 2024 연하장 생성기 🎊")

# 입력 필드
name = st.text_input("받는 분의 이름을 입력하세요")
style = st.selectbox("어떤 스타일로 작성할까요?", ["정중하게", "친근하게"])

# 폰트 리스트
fonts = [
    'Nanum Pen Script',
    'Gaegu',
    'Hi Melody',
    'Dongle',
    'Gamja Flower',
    'East Sea Dokdo'
]

if st.button("연하장 생성하기"):
    if name:
        st.markdown("---")
        
        # 랜덤 폰트 선택
        random_font = random.choice(fonts)
        
        # 현재 날짜
        current_date = datetime.now().strftime("%Y년 %m월 %d일")
        
        # 스타일에 따른 인사말 선택
        greeting = random.choice(formal_greetings) if style == "정중하게" else random.choice(casual_greetings)
        
        # 동적 스타일 생성
        dynamic_style = f"""
        <style>
        .handwriting-{random_font.lower().replace(' ', '-')} {{
            font-family: '{random_font}', cursive !important;
            font-size: 28px !important;
            line-height: 1.8 !important;
            color: #1a1a1a !important;
        }}
        .name {{
            font-size: 32px !important;
            margin-bottom: 20px !important;
        }}
        .date {{
            font-size: 24px !important;
            margin-top: 30px !important;
            text-align: right !important;
        }}
        </style>
        """
        
        # 연하장 내용 생성
        message = f"""
        {dynamic_style}
        <div class="letter-container">
            <div class="handwriting-{random_font.lower().replace(' ', '-')}">
                <div class="name">{name}님께,</div>
                {greeting}
                <div class="date">{current_date}</div>
            </div>
        </div>
        """
        
        st.markdown(message, unsafe_allow_html=True)
        
        # 디버깅용 (선택된 폰트 확인)
        st.write(f"선택된 폰트: {random_font}")
    else:
        st.error("이름을 입력해주세요!")