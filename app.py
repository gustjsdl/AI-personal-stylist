import streamlit as st

# -----------------------------
# 페이지 기본 설정
# -----------------------------
st.set_page_config(
    page_title="AI Personal Stylist",
    page_icon="👗",
    layout="wide"
)

# -----------------------------
# CSS 디자인
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: #f7f7f5;
    }

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 8px;
        color: #222222;
    }

    .sub-title {
        text-align: center;
        font-size: 16px;
        color: #777777;
        margin-bottom: 35px;
    }

    .input-card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0 3px 15px rgba(0,0,0,0.06);
    }

    .section-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 15px;
        color: #222222;
    }

    .result-card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        min-height: 210px;
        box-shadow: 0 3px 15px rgba(0,0,0,0.06);
        border: 1px solid #eeeeee;
    }

    .result-icon {
        font-size: 38px;
        margin-bottom: 10px;
    }

    .result-title {
        font-size: 17px;
        font-weight: 700;
        color: #222222;
        margin-bottom: 8px;
    }

    .result-text {
        font-size: 15px;
        color: #555555;
        line-height: 1.6;
    }

    .analysis-card {
        background: #ffffff;
        padding: 24px;
        border-radius: 18px;
        margin-top: 15px;
        box-shadow: 0 3px 15px rgba(0,0,0,0.05);
    }

    .analysis-title {
        font-size: 19px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .analysis-text {
        color: #555555;
        line-height: 1.7;
    }

    .recommendation-header {
        text-align: center;
        font-size: 30px;
        font-weight: 700;
        margin-top: 35px;
        margin-bottom: 25px;
    }

    .warning-box {
        background: #fff3f3;
        border: 1px solid #f0b5b5;
        color: #b83232;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin: 20px 0;
    }

    div.stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 12px;
        font-size: 17px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# 스타일별 기본 코디
# -----------------------------
style_outfits = {

    "캐주얼": {
        "상의": "오버핏 코튼 티셔츠",
        "하의": "스트레이트 데님 팬츠",
        "신발": "화이트 스니커즈",
        "액세서리": "심플한 크로스백과 미니멀 주얼리"
    },

    "미니멀": {
        "상의": "깔끔한 무지 셔츠",
        "하의": "와이드 슬랙스",
        "신발": "블랙 로퍼",
        "액세서리": "심플한 가죽 가방과 실버 시계"
    },

    "스트릿": {
        "상의": "그래픽 오버핏 후드티",
        "하의": "카고 팬츠",
        "신발": "청키 스니커즈",
        "액세서리": "볼캡과 실버 체인 목걸이"
    },

    "클래식": {
        "상의": "테일러드 셔츠",
        "하의": "핀턱 슬랙스",
        "신발": "클래식 로퍼",
        "액세서리": "가죽 벨트와 클래식 시계"
    },

    "페미닌": {
        "상의": "실루엣이 돋보이는 블라우스",
        "하의": "플레어 미디 스커트",
        "신발": "메리제인 슈즈",
        "액세서리": "작은 숄더백과 진주 귀걸이"
    },

    "스포티": {
        "상의": "기능성 크롭 집업",
        "하의": "조거 팬츠",
        "신발": "러닝 스니커즈",
        "액세서리": "미니 백팩과 스포츠 워치"
    }
}


# -----------------------------
# 체형별 추천
# -----------------------------
body_type_tips = {

    "상체가 발달한 체형": {
        "상의": "어깨와 가슴 부분이 지나치게 강조되지 않는 V넥 또는 오픈카라 디자인",
        "하의": "하체에 적당한 볼륨을 더하는 와이드 팬츠",
        "분석": "상체의 볼륨감을 자연스럽게 분산하고 하체에 균형을 더하는 실루엣을 추천했어요."
    },

    "하체가 발달한 체형": {
        "상의": "밝은 컬러나 포인트 디테일이 있는 상의",
        "하의": "다리 라인을 자연스럽게 커버하는 스트레이트 또는 와이드 팬츠",
        "분석": "시선을 상체로 분산하고 하체의 실루엣은 자연스럽게 정돈해 균형 잡힌 비율을 만들어요."
    },

    "전체적으로 균형 잡힌 체형": {
        "상의": "몸의 실루엣을 살려주는 적당히 여유 있는 상의",
        "하의": "스트레이트, 와이드, 슬림 등 다양한 실루엣",
        "분석": "전체적인 비율이 균형 잡혀 있어 다양한 실루엣을 자연스럽게 소화할 수 있어요."
    },

    "마른 체형": {
        "상의": "레이어드나 니트처럼 볼륨감을 더할 수 있는 상의",
        "하의": "와이드 또는 플리츠 디테일이 있는 하의",
        "분석": "레이어드와 볼륨감 있는 아이템을 활용해 전체적인 실루엣에 자연스러운 입체감을 더했어요."
    },

    "잘 모르겠음": {
        "상의": "체형에 크게 구애받지 않는 깔끔한 기본 상의",
        "하의": "스트레이트 핏의 기본 팬츠",
        "분석": "체형 정보가 확실하지 않기 때문에 다양한 체형에 무난하게 어울리는 기본 실루엣을 선택했어요."
    }
}


# -----------------------------
# 상황별 추천
# -----------------------------
situation_tips = {

    "학교": "편안하면서도 깔끔한 데일리룩을 중심으로 구성했어요.",
    "데이트": "부드럽고 세련된 분위기를 살려 상대방에게 좋은 인상을 줄 수 있도록 구성했어요.",
    "면접": "단정하고 신뢰감 있는 인상을 줄 수 있도록 깔끔한 실루엣을 우선했어요.",
    "친구와의 약속": "편안함과 개성을 동시에 살릴 수 있는 스타일로 구성했어요.",
    "특별한 날": "평소보다 조금 더 포인트가 있고 완성도 높은 스타일을 추천했어요."
}


# -----------------------------
# 색상별 추천
# -----------------------------
color_tips = {

    "블랙": "블랙은 대부분의 색상과 잘 어울리며 세련되고 도시적인 느낌을 만들어줘요.",

    "화이트": "화이트는 깨끗하고 밝은 인상을 주며 다양한 색상과 조화롭게 매치할 수 있어요.",

    "베이지": "베이지는 부드럽고 따뜻한 분위기를 만들어 데일리 스타일에 활용하기 좋아요.",

    "네이비": "네이비는 차분하고 신뢰감 있는 분위기를 만들어 클래식한 스타일에 특히 잘 어울려요.",

    "그레이": "그레이는 차분하고 모던한 분위기를 만들어 미니멀 스타일에 활용하기 좋아요.",

    "핑크": "핑크는 부드럽고 사랑스러운 분위기를 만들어 페미닌한 스타일에 잘 어울려요.",

    "블루": "블루는 시원하고 산뜻한 분위기를 만들어 캐주얼한 스타일에 활용하기 좋아요.",

    "그린": "그린은 자연스럽고 개성 있는 분위기를 만들어 포인트 컬러로 활용하기 좋아요."
}


# -----------------------------
# 상황에 따른 아이템 변경
# -----------------------------
def apply_situation(outfit, situation):

    result = outfit.copy()

    if situation == "면접":
        result["상의"] = "깔끔한 화이트 셔츠"
        result["하의"] = "테일러드 슬랙스"
        result["신발"] = "단정한 블랙 로퍼"
        result["액세서리"] = "심플한 시계와 미니멀한 가방"

    elif situation == "데이트":
        result["신발"] = "깔끔한 메리제인 또는 로퍼"
        result["액세서리"] = "작은 숄더백과 포인트 주얼리"

    elif situation == "특별한 날":
        result["신발"] = "포인트가 있는 플랫슈즈 또는 로퍼"
        result["액세서리"] = "포인트 주얼리와 미니 숄더백"

    elif situation == "학교":
        result["신발"] = "편안한 화이트 스니커즈"

    elif situation == "친구와의 약속":
        result["신발"] = "캐주얼 스니커즈"
        result["액세서리"] = "미니 크로스백과 심플한 액세서리"

    return result


# -----------------------------
# 제목
# -----------------------------
st.markdown(
    '<div class="main-title">AI Personal Stylist</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    '나에게 어울리는 스타일을 찾아주는 AI 퍼스널 스타일리스트'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# 입력 영역
# -----------------------------
st.markdown(
    '<div class="input-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">✦ 나의 스타일 정보</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "성별",
        [
            "선택해주세요",
            "여성",
            "남성",
            "상관없음"
        ]
    )

    body_type = st.selectbox(
        "체형",
        [
            "선택해주세요",
            "상체가 발달한 체형",
            "하체가 발달한 체형",
            "전체적으로 균형 잡힌 체형",
            "마른 체형",
            "잘 모르겠음"
        ]
    )

    style = st.selectbox(
        "선호하는 패션 스타일",
        [
            "선택해주세요",
            "캐주얼",
            "미니멀",
            "스트릿",
            "클래식",
            "페미닌",
            "스포티"
        ]
    )

with col2:

    favorite_color = st.selectbox(
        "좋아하는 색상",
        [
            "선택해주세요",
            "블랙",
            "화이트",
            "베이지",
            "네이비",
            "그레이",
            "핑크",
            "블루",
            "그린"
        ]
    )

    situation = st.selectbox(
        "옷을 입을 상황",
        [
            "선택해주세요",
            "학교",
            "데이트",
            "면접",
            "친구와의 약속",
            "특별한 날"
        ]
    )

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# 추천 버튼
# -----------------------------
recommend = st.button(
    "✨ 코디 추천받기",
    use_container_width=True
)


# -----------------------------
# 추천 기능
# -----------------------------
if recommend:

    # 모든 항목 선택 여부 확인
    if (
        gender == "선택해주세요"
        or body_type == "선택해주세요"
        or style == "선택해주세요"
        or favorite_color == "선택해주세요"
        or situation == "선택해주세요"
    ):

        st.markdown(
            '<div class="warning-box">'
            '⚠️ 모든 항목을 선택해주세요.<br>'
            '성별, 체형, 선호 스타일, 좋아하는 색상, 상황을 모두 선택해야 추천을 받을 수 있어요.'
            '</div>',
            unsafe_allow_html=True
        )

    else:

        # 기본 스타일 코디 가져오기
        outfit = style_outfits[style]

        # 상황 반영
        outfit = apply_situation(outfit, situation)

        # 체형 정보
        body_info = body_type_tips[body_type]

        # 체형에 따른 상의/하의 일부 반영
        if situation != "면접":
            outfit["상의"] = body_info["상의"]

        if body_type != "전체적으로 균형 잡힌 체형":
            outfit["하의"] = body_info["하의"]

        # 결과 제목
        st.markdown(
            '<div class="recommendation-header">'
            '✨ 당신을 위한 추천 코디'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div style="text-align:center; color:#777; margin-bottom:25px;">'
            f'{gender} · {body_type} · {style} · {favorite_color} · {situation}'
            f'</div>',
            unsafe_allow_html=True
        )

        # -----------------------------
        # 코디 카드
        # -----------------------------
        c1, c2, c3, c4 = st.columns(4)

        cards = [
            ("👕", "상의", outfit["상의"]),
            ("👖", "하의", outfit["하의"]),
            ("👟", "신발", outfit["신발"]),
            ("👜", "액세서리", outfit["액세서리"])
        ]

        columns = [c1, c2, c3, c4]

        for col, card in zip(columns, cards):

            icon, title, text = card

            with col:

                st.markdown(
                    f"""
                    <div class="result-card">
                        <div class="result-icon">{icon}</div>
                        <div class="result-title">{title}</div>
                        <div class="result-text">{text}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # -----------------------------
        # 분석 영역
        # -----------------------------
        st.markdown(
            '<div class="recommendation-header">'
            '🔍 스타일 분석'
            '</div>',
            unsafe_allow_html=True
        )

        a1, a2, a3 = st.columns(3)

        with a1:
            st.markdown(
                f"""
                <div class="analysis-card">
                    <div class="analysis-title">👤 체형 분석</div>
                    <div class="analysis-text">
                        <b>{body_type}</b>을 고려했어요.<br><br>
                        {body_info["분석"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with a2:
            st.markdown(
                f"""
                <div class="analysis-card">
                    <div class="analysis-title">🎨 컬러 분석</div>
                    <div class="analysis-text">
                        선호하는 색상인 <b>{favorite_color}</b>을
                        코디의 핵심 컬러로 활용했어요.<br><br>
                        {color_tips[favorite_color]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with a3:
            st.markdown(
                f"""
                <div class="analysis-card">
                    <div class="analysis-title">✨ 스타일 분석</div>
                    <div class="analysis-text">
                        선호 스타일은 <b>{style}</b>이에요.<br><br>
                        {situation_tips[situation]}<br><br>
                        {style} 특유의 분위기를 유지하면서
                        {body_type}에 어울리는 실루엣을 적용했어요.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # -----------------------------
        # 최종 추천 이유
        # -----------------------------
        st.markdown(
            f"""
            <div class="analysis-card">
                <div class="analysis-title">
                    💡 왜 이 코디를 추천했을까요?
                </div>

                <div class="analysis-text">
                    <b>① 체형</b><br>
                    {body_info["분석"]}
                    <br><br>

                    <b>② 컬러</b><br>
                    {color_tips[favorite_color]}
                    <br><br>

                    <b>③ 스타일</b><br>
                    {style} 스타일의 특징을 살려
                    사용자가 원하는 패션 분위기를 반영했어요.
                    <br><br>

                    <b>④ 상황</b><br>
                    {situation_tips[situation]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            "<br><br>",
            unsafe_allow_html=True
        )

        st.success(
            f"✨ {favorite_color} 컬러를 중심으로 한 "
            f"{style} 스타일의 {situation} 코디가 완성되었어요!"
        )
