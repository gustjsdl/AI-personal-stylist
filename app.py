import streamlit as st

# ==========================================
# 페이지 설정
# ==========================================

st.set_page_config(
    page_title="AI Personal Stylist",
    page_icon="✨",
    layout="centered"
)

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #f8f7f5;
}

.main {
    max-width: 800px;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    color: #222;
    margin-top: 50px;
}

.subtitle {
    text-align: center;
    color: #888;
    font-size: 16px;
    margin-bottom: 40px;
}

.step {
    text-align: center;
    color: #999;
    font-size: 14px;
    margin-bottom: 15px;
}

.question {
    text-align: center;
    font-size: 28px;
    font-weight: 700;
    color: #222;
    margin-bottom: 35px;
}

.option-button {
    width: 100%;
}

.result-card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}

.result-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}

.result-text {
    color: #555;
    line-height: 1.7;
}

.progress-text {
    text-align: center;
    color: #999;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 세션 상태 초기화
# ==========================================

if "step" not in st.session_state:
    st.session_state.step = 1

if "gender" not in st.session_state:
    st.session_state.gender = None

if "body_type" not in st.session_state:
    st.session_state.body_type = None

if "style" not in st.session_state:
    st.session_state.style = None

if "color" not in st.session_state:
    st.session_state.color = None

if "situation" not in st.session_state:
    st.session_state.situation = None


# ==========================================
# 공통 함수
# ==========================================

def next_step():
    st.session_state.step += 1


def select_option(key, value):
    st.session_state[key] = value
    st.session_state.step += 1


# ==========================================
# 제목
# ==========================================

st.markdown(
    '<div class="title">AI Personal Stylist</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">나에게 어울리는 스타일을 찾아보세요</div>',
    unsafe_allow_html=True
)


# ==========================================
# STEP 1 : 성별
# ==========================================

if st.session_state.step == 1:

    st.markdown(
        '<div class="step">STEP 1 / 5</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="question">성별을 선택해주세요</div>',
        unsafe_allow_html=True
    )

    if st.button("여성", use_container_width=True):
        select_option("gender", "여성")

    if st.button("남성", use_container_width=True):
        select_option("gender", "남성")

    if st.button("상관없음", use_container_width=True):
        select_option("gender", "상관없음")


# ==========================================
# STEP 2 : 체형
# ==========================================

elif st.session_state.step == 2:

    st.markdown(
        '<div class="step">STEP 2 / 5</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="question">체형을 선택해주세요</div>',
        unsafe_allow_html=True
    )

    options = [
        "상체가 발달한 체형",
        "하체가 발달한 체형",
        "전체적으로 균형 잡힌 체형",
        "마른 체형",
        "잘 모르겠음"
    ]

    for option in options:
        if st.button(option, use_container_width=True):
            select_option("body_type", option)


# ==========================================
# STEP 3 : 패션 스타일
# ==========================================

elif st.session_state.step == 3:

    st.markdown(
        '<div class="step">STEP 3 / 5</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="question">선호하는 패션 스타일은?</div>',
        unsafe_allow_html=True
    )

    options = [
        "캐주얼",
        "미니멀",
        "스트릿",
        "클래식",
        "페미닌",
        "스포티"
    ]

    for option in options:
        if st.button(option, use_container_width=True):
            select_option("style", option)


# ==========================================
# STEP 4 : 좋아하는 색상
# ==========================================

elif st.session_state.step == 4:

    st.markdown(
        '<div class="step">STEP 4 / 5</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="question">좋아하는 색상을 선택해주세요</div>',
        unsafe_allow_html=True
    )

    colors = [
        "블랙",
        "화이트",
        "베이지",
        "네이비",
        "그레이",
        "핑크",
        "블루",
        "그린"
    ]

    for color in colors:
        if st.button(color, use_container_width=True):
            select_option("color", color)


# ==========================================
# STEP 5 : 상황
# ==========================================

elif st.session_state.step == 5:

    st.markdown(
        '<div class="step">STEP 5 / 5</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="question">어떤 상황에 입을 옷인가요?</div>',
        unsafe_allow_html=True
    )

    situations = [
        "학교",
        "데이트",
        "면접",
        "친구와의 약속",
        "특별한 날"
    ]

    for situation in situations:
        if st.button(situation, use_container_width=True):
            select_option("situation", situation)


# ==========================================
# 스타일별 기본 코디
# ==========================================

style_outfits = {

    "캐주얼": {
        "상의": "오버핏 코튼 티셔츠",
        "하의": "스트레이트 데님 팬츠",
        "신발": "화이트 스니커즈",
        "액세서리": "미니 크로스백"
    },

    "미니멀": {
        "상의": "깔끔한 무지 셔츠",
        "하의": "와이드 슬랙스",
        "신발": "블랙 로퍼",
        "액세서리": "미니멀한 가죽 가방"
    },

    "스트릿": {
        "상의": "오버핏 후드티",
        "하의": "카고 팬츠",
        "신발": "청키 스니커즈",
        "액세서리": "볼캡과 실버 체인"
    },

    "클래식": {
        "상의": "테일러드 셔츠",
        "하의": "핀턱 슬랙스",
        "신발": "클래식 로퍼",
        "액세서리": "가죽 시계"
    },

    "페미닌": {
        "상의": "실루엣이 돋보이는 블라우스",
        "하의": "플레어 미디 스커트",
        "신발": "메리제인 슈즈",
        "액세서리": "진주 귀걸이와 숄더백"
    },

    "스포티": {
        "상의": "기능성 집업",
        "하의": "조거 팬츠",
        "신발": "러닝 스니커즈",
        "액세서리": "미니 백팩"
    }
}


# ==========================================
# 체형 분석
# ==========================================

body_analysis = {

    "상체가 발달한 체형":
        "상체의 볼륨감을 자연스럽게 분산시키고 하체에 적당한 볼륨을 더하는 실루엣을 추천했어요.",

    "하체가 발달한 체형":
        "시선을 상체로 분산시키고 하체는 자연스럽게 정돈되는 실루엣을 추천했어요.",

    "전체적으로 균형 잡힌 체형":
        "전체적인 비율이 균형 잡혀 있어 다양한 실루엣을 자연스럽게 활용할 수 있어요.",

    "마른 체형":
        "레이어드와 볼륨감 있는 아이템을 활용해 전체적인 실루엣에 입체감을 더했어요.",

    "잘 모르겠음":
        "체형에 크게 구애받지 않는 기본적인 실루엣을 중심으로 추천했어요."
}


# ==========================================
# 컬러 분석
# ==========================================

color_analysis = {

    "블랙":
        "세련되고 도시적인 분위기를 만들어주는 색상이에요.",

    "화이트":
        "깨끗하고 밝은 인상을 만들어주는 색상이에요.",

    "베이지":
        "부드럽고 따뜻한 분위기를 만들어주는 색상이에요.",

    "네이비":
        "차분하고 신뢰감 있는 분위기를 만들어주는 색상이에요.",

    "그레이":
        "모던하고 차분한 느낌을 만들어주는 색상이에요.",

    "핑크":
        "부드럽고 사랑스러운 분위기를 만들어주는 색상이에요.",

    "블루":
        "시원하고 산뜻한 분위기를 만들어주는 색상이에요.",

    "그린":
        "자연스럽고 개성 있는 분위기를 만들어주는 색상이에요."
}


# ==========================================
# 상황별 분석
# ==========================================

situation_analysis = {

    "학교":
        "편안하면서도 깔끔한 데일리룩을 추천했어요.",

    "데이트":
        "부드럽고 세련된 분위기를 연출할 수 있도록 구성했어요.",

    "면접":
        "단정하고 신뢰감 있는 인상을 줄 수 있도록 구성했어요.",

    "친구와의 약속":
        "편안함과 개성을 동시에 살릴 수 있도록 구성했어요.",

    "특별한 날":
        "평소보다 조금 더 포인트 있고 완성도 높은 스타일을 추천했어요."
}


# ==========================================
# STEP 6 : 결과
# ==========================================

elif st.session_state.step == 6:

    st.markdown(
        '<div class="step">YOUR RESULT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="question">✨ 당신을 위한 코디</div>',
        unsafe_allow_html=True
    )

    gender = st.session_state.gender
    body = st.session_state.body_type
    style = st.session_state.style
    color = st.session_state.color
    situation = st.session_state.situation

    outfit = style_outfits[style].copy()

    # 상황에 따른 수정
    if situation == "면접":
        outfit["상의"] = "깔끔한 화이트 셔츠"
        outfit["하의"] = "테일러드 슬랙스"
        outfit["신발"] = "단정한 블랙 로퍼"
        outfit["액세서리"] = "심플한 시계와 가죽 가방"

    elif situation == "데이트":
        outfit["신발"] = "메리제인 또는 깔끔한 로퍼"
        outfit["액세서리"] = "작은 숄더백과 포인트 주얼리"

    elif situation == "특별한 날":
        outfit["액세서리"] = "포인트 주얼리와 미니 숄더백"

    # ======================================
    # 추천 코디 카드
    # ======================================

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="result-card">
            <div class="result-title">👕 상의</div>
            <div class="result-text">{outfit["상의"]}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="result-card">
            <div class="result-title">👖 하의</div>
            <div class="result-text">{outfit["하의"]}</div>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(f"""
        <div class="result-card">
            <div class="result-title">👟 신발</div>
            <div class="result-text">{outfit["신발"]}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="result-card">
            <div class="result-title">👜 액세서리</div>
            <div class="result-text">{outfit["액세서리"]}</div>
        </div>
        """, unsafe_allow_html=True)


    # ======================================
    # 체형 분석
    # ======================================

    st.markdown(f"""
    <div class="result-card">
        <div class="result-title">👤 체형 분석</div>
        <div class="result-text">
            <b>{body}</b><br><br>
            {body_analysis[body]}
        </div>
    </div>
    """, unsafe_allow_html=True)


    # ======================================
    # 컬러 분석
    # ======================================

    st.markdown(f"""
    <div class="result-card">
        <div class="result-title">🎨 컬러 분석</div>
        <div class="result-text">
            선호 색상 <b>{color}</b>을 코디의 포인트 컬러로 활용했어요.<br><br>
            {color_analysis[color]}
        </div>
    </div>
    """, unsafe_allow_html=True)


    # ======================================
    # 스타일 분석
    # ======================================

    st.markdown(f"""
    <div class="result-card">
        <div class="result-title">✨ 스타일 분석</div>
        <div class="result-text">
            <b>{style}</b> 스타일을 기본으로 구성했어요.<br><br>
            {situation_analysis[situation]}
        </div>
    </div>
    """, unsafe_allow_html=True)


    # ======================================
    # 선택 정보
    # ======================================

    st.markdown(f"""
    <div class="result-card">
        <div class="result-title">📋 나의 스타일 정보</div>
        <div class="result-text">
            성별 : {gender}<br>
            체형 : {body}<br>
            선호 스타일 : {style}<br>
            좋아하는 색상 : {color}<br>
            상황 : {situation}
        </div>
    </div>
    """, unsafe_allow_html=True)


    # ======================================
    # 다시 하기
    # ======================================

    if st.button("↩ 다시 스타일 진단하기", use_container_width=True):

        st.session_state.step = 1
        st.session_state.gender = None
        st.session_state.body_type = None
        st.session_state.style = None
        st.session_state.color = None
        st.session_state.situation = None

        st.rerun()

