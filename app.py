import streamlit as st
from datetime import datetime
import random

# OpenAI 임포트 시도
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    st.warning("OpenAI 패키지가 설치되지 않았습니다. AI 기능이 비활성화됩니다.")

# 페이지 설정
st.set_page_config(
    page_title="2024 연하장 생성기",
    page_icon="🎊",
    layout="centered"
)

# OpenAI API 키 설정
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
except Exception as e:
    st.error("OpenAI API 키가 설정되지 않았습니다. .streamlit/secrets.toml 파일을 확인해주세요.")

# 기본 인사말 리스트
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

def generate_ai_greeting(name: str, style: str, relationship: Optional[str] = None) -> str:
    if not OPENAI_AVAILABLE:
        return random.choice(formal_greetings if style == "정중하게" else casual_greetings)
    
    try:
        if not openai.api_key:
            raise ValueError("API 키가 설정되지 않았습니다.")
            
        prompt = f"""
        {name}님께 보내는 2024년 새해 인사 메시지를 작성해주세요.
        스타일: {'정중한' if style == '정중하게' else '친근한'}
        관계: {relationship if relationship else '일반적인'}
        조건:
        - 3문장 이내로 작성
        - 새해 인사에 어울리는 따뜻한 메시지
        - {'존댓말 사용' if style == '정중하게' else '반말 사용'}
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 따뜻한 새해 인사말을 작성하는 전문가입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        return random.choice(formal_greetings if style == "정중하게" else casual_greetings)

# CSS 스타일
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&family=Gaegu&family=Hi+Melody&family=Dongle&family=Gamja+Flower&family=East+Sea+Dokdo&display=swap');
    
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    
    .main-title {
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# 메인 앱
def main():
    st.markdown("<h1 class='main-title'>🎊 2024 연하장 생성기 🎊</h1>", unsafe_allow_html=True)
    
    # 입력 섹션
    with st.form("letter_form"):
        name = st.text_input("받는 분의 이름을 입력하세요")
        style = st.selectbox("어떤 스타일로 작성할까요?", ["정중하게", "친근하게"])
        
        # 추가 옵션
        use_ai = st.checkbox("AI가 작성한 메시지 사용하기", value=True)
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
                
            # 랜덤 선택
            random_font = random.choice(fonts)
            random_bg = random.choice(backgrounds)
            
            # 인사말 생성
            greeting = generate_ai_greeting(name, style, relationship) if use_ai else \
                      random.choice(formal_greetings if style == "정중하게" else casual_greetings)
            
            # 현재 날짜
            current_date = datetime.now().strftime("%Y년 %m월 %d일")
            
            # 동적 스타일 및 메시지 생성
            create_letter(name, greeting, current_date, random_font, random_bg)
            
            if use_ai:
                st.caption("✨ AI가 작성한 특별한 메시지입니다.")

def create_letter(name, greeting, date, font, bg):
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

# 사용 안내
with st.expander("💡 사용 방법"):
    st.markdown("""
    1. 받는 분의 이름을 입력하세요.
    2. 원하는 스타일을 선택하세요.
    3. 추가 옵션에서 AI 메시지 사용 여부와 관계를 선택할 수 있습니다.
    4. '연하장 생성하기' 버튼을 클릭하면 새로운 연하장이 생성됩니다.
    5. 마음에 들 때까지 여러 번 생성해보세요!
    """)

if __name__ == "__main__":
    main()