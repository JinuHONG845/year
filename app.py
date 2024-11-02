import streamlit as st
from datetime import datetime
import random
from typing import Optional

# 페이지 설정
st.set_page_config(
    page_title="홍진우가 만든 연하장 자동 프로그램",
    page_icon="🎊",
    layout="centered"
)

# CSS 스타일
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&family=Gaegu&family=Hi+Melody&family=Dongle&family=Gamja+Flower&family=East+Sea+Dokdo&display=swap');
    
    .main-title {
        text-align: center;
        color: #1E4174;
        font-size: 2.2em;
        margin-bottom: 2rem;
        padding: 20px;
        background: linear-gradient(to right, #f8f9fa, #e9ecef, #f8f9fa);
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    
    .letter-container {
        background-size: cover;
        padding: 40px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        position: relative;
    }
    
    .handwriting {
        font-family: var(--font-family) !important;
        font-size: 28px !important;
        line-height: 1.8 !important;
        color: #1a1a1a !important;
        position: relative;
        z-index: 1;
    }
    </style>
""", unsafe_allow_html=True)

# 배경 이미지 리스트
backgrounds = [
    "https://img.freepik.com/free-photo/crumpled-paper-background_1373-431.jpg",
    "https://img.freepik.com/free-photo/design-space-paper-textured-background_53876-42312.jpg",
    "https://img.freepik.com/free-photo/white-paper-texture_1194-5416.jpg",
    "https://img.freepik.com/free-photo/beige-paper-texture_95678-72.jpg",
    "https://img.freepik.com/free-photo/brown-paper-texture_95678-75.jpg"
]

# 폰트 리스트
fonts = [
    'Nanum Pen Script',
    'Gaegu',
    'Hi Melody',
    'Dongle',
    'Gamja Flower',
    'East Sea Dokdo'
]

# 정중한 인사말 리스트
formal_greetings = [
    """
    희망찬 새해가 밝았습니다.
    지난 한 해 동안 베풀어주신 은혜에 깊이 감사드립니다.
    새해에도 변함없는 건강과 행운이 함께하시길 진심으로 기원드립니다.
    소망하시는 모든 일들이 이루어지는 축복된 한 해 되시길 바랍니다.
    늘 행복과 기쁨이 가득한 나날 보내시길 기원합니다.
    """,
    # ... 다른 정중한 인사말들 ...
]

# 친근한 인사말 리스트
casual_greetings = [
    """
    어느새 2024년이 밝았어!
    지난 한 해 동안 정말 고마웠어.
    새해에도 우리 더 재미있고 행복하게 지내자!
    네가 꿈꾸던 모든 일들이 다 이루어졌으면 좋겠어.
    올해도 우리 우정 변함없이 이어가자!
    """,
    # ... 다른 친근한 인사말들 ...
]

def create_letter(name: str, greeting: str, date: str, font: str, bg: str):
    """연하장 HTML을 생성하고 표시합니다."""
    dynamic_style = f"""
    <style>
    .letter-container-{font.lower().replace(' ', '-')} {{
        background-image: url('{bg}');
        background-size: cover;
        padding: 40px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        position: relative;
    }}
    
    .letter-container-{font.lower().replace(' ', '-')}::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(255, 255, 255, 0.4);
        border-radius: 15px;
    }}
    
    .handwriting-{font.lower().replace(' ', '-')} {{
        font-family: '{font}', cursive !important;
        font-size: 28px !important;
        line-height: 1.8 !important;
        color: #1a1a1a !important;
        position: relative;
        z-index: 1;
    }}
    </style>
    """
    
    message = f"""
    {dynamic_style}
    <div class="letter-container-{font.lower().replace(' ', '-')}">
        <div class="handwriting-{font.lower().replace(' ', '-')}">
            <div class="name">{name}님께,</div>
            {greeting}
            <div class="date">{date}</div>
        </div>
    </div>
    """
    
    st.markdown(message, unsafe_allow_html=True)

def main():
    # 메인 타이틀
    st.markdown("<h1 class='main-title'>🎊 홍진우가 만든 연하장 자동 프로그램 🎊</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>소중한 분들께 마음을 전하세요</p>", unsafe_allow_html=True)
    
    # 입력 폼
    with st.form("letter_form"):
        name = st.text_input("받는 분의 이름을 입력하세요")
        style = st.selectbox("어떤 스타일로 작성할까요?", ["정중하게", "친근하게"])
        relationship = st.selectbox(
            "받는 분과의 관계",
            ["가족", "친구", "동료", "선생님", "기타"]
        )
        
        if relationship == "기타":
            relationship = st.text_input("관계를 직접 입력해주세요")
        
        submitted = st.form_submit_button("연하장 생성하기")
        
        if submitted:
            if not name:
                st.error("이름을 입력해주세요!")
                return
                
            random_font = random.choice(fonts)
            random_bg = random.choice(backgrounds)
            greeting = random.choice(formal_greetings if style == "정중하게" else casual_greetings)
            current_date = datetime.now().strftime("%Y년 %m월 %d일")
            
            create_letter(name, greeting.strip(), current_date, random_font, random_bg)

    # 사용 안내
    with st.expander("💡 사용 방법"):
        st.markdown("""
        1. 받는 분의 이름을 입력하세요.
        2. 원하는 스타일을 선택하세요.
        3. 받는 분과의 관계를 선택하세요.
        4. '연하장 생성하기' 버튼을 클릭하면 새로운 연하장이 생성됩니다.
        5. 마음에 들 때까지 여러 번 생성해보세요!
        """)

if __name__ == "__main__":
    main()