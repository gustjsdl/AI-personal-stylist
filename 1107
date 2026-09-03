import streamlit as st

# --------------------------------------------------
# 페이지 기본 설정
# --------------------------------------------------

st.set_page_config(
    page_title="AI Personal Stylist",
    page_icon="👗",
    layout="centered"
)

# --------------------------------------------------
# 스타일
# --------------------------------------------------

st.markdown("""
<style>
    .main {
        background-color: #faf9f7;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777777;
        font-size: 17px;
        margin-bottom: 35px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .result-box {
        padding: 25px;
        border-radius: 18px;
        background-color: white;
        border: 1px solid #e5e5e5;
        margin-top: 20px;
    }

    .outfit-item {
        padding: 18px;
        border-radius: 14px;
        background-color: #f7f5f2;
        text-align: center;
        margin-bottom: 10px;
    }

    .item-title {
        font-size: 14px;
        color: #777777;
        margin-bottom: 5px;
    }

    .item-content {
        font-size: 18px;
        font-weight: 600;
    }

    .reason {
        padding: 18px;
        border-radius: 14px;
        background-color: #f8f8f8;
        line-height: 1.7;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# 제목
# --------------------------------------------------

st.markdown(
    '<div class="title">AI Personal Stylist 👗</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">당신의 체형과 취향, 상황에 맞는 스타일을 추천해드립니다.</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# 사용자 정보 입력
# --------------------------------------------------

st.markdown(
    '<div class="section-title">01. 기본 정보</div>',
    unsafe_allow_html=True
)

gender = st.selectbox(
    "성별",
    ["선택해주세요", "여성", "남성", "상관없음"]
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


# --------------------------------------------------
# 스타일 입력
# --------------------------------------------------

st.markdown(
    '<div class="section-title">02. 나의 스타일</div>',
    unsafe_allow_html=True
)

style = st.selectbox(
    "선호하는 스타일",
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

color = st.selectbox(
    "선호하는 색상",
    [
        "선택해주세요",
        "블랙",
        "화이트",
        "그레이",
        "네이비",
        "베이지",
        "브라운",
        "파스텔",
        "다양한 색상"
    ]
)


# --------------------------------------------------
# 상황 입력
# --------------------------------------------------

st.markdown(
    '<div class="section-title">03. 오늘의 상황</div>',
    unsafe_allow_html=True
)

occasion = st.selectbox(
    "어떤 상황에 입을 옷인가요?",
    [
        "선택해주세요",
        "학교",
        "데이트",
        "면접",
        "친구와의 약속",
        "특별한 날"
    ]
)


# --------------------------------------------------
# 추천 함수
# --------------------------------------------------

def recommend_outfit(gender, body_type, style, color, occasion):

    # 기본 추천
    top = "깔끔한 기본 셔츠"
    bottom = "스트레이트 팬츠"
    shoes = "미니멀 스니커즈"
    accessory = "심플한 시계"

    # 스타일에 따른 추천
    if style == "캐주얼":
        top = "오버핏 셔츠 또는 기본 티셔츠"
        bottom = "스트레이트 데님"
        shoes = "화이트 스니커즈"
        accessory = "캐주얼 캡 또는 미니 크로스백"

    elif style == "미니멀":
        top = "화이트 셔츠 또는 니트"
        bottom = "블랙 와이드 슬랙스"
        shoes = "심플한 로퍼"
        accessory = "미니멀한 시계"

    elif style == "스트릿":
        top = "그래픽 티셔츠 또는 오버핏 후드"
        bottom = "와이드 카고 팬츠"
        shoes = "청키 스니커즈"
        accessory = "볼캡 또는 실버 액세서리"

    elif style == "클래식":
        top = "셔츠 + 니트 베스트"
        bottom = "테일러드 슬랙스"
        shoes = "가죽 로퍼"
        accessory = "가죽 벨트와 시계"

    elif style == "페미닌":
        top = "블라우스 또는 슬림 니트"
        bottom = "A라인 스커트"
        shoes = "플랫슈즈 또는 메리제인"
        accessory = "작은 숄더백"

    elif style == "스포티":
        top = "기능성 반팔 티셔츠"
        bottom = "조거 팬츠"
        shoes = "러닝 스니커즈"
        accessory = "스포츠 백"

    # 체형에 따른 수정
    if body_type == "상체가 발달한 체형":
        body_reason = "상체의 볼륨감을 고려해 하체에 자연스럽게 시선이 이동하도록 밸런스를 맞췄습니다."
        
        if style in ["캐주얼", "스트릿"]:
            top = "어깨선이 자연스러운 여유 있는 티셔츠"
        else:
            top = "세로선이 강조되는 깔끔한 셔츠"

        bottom = "와이드 또는 스트레이트 팬츠"

    elif body_type == "하체가 발달한 체형":
        body_reason = "하체의 실루엣을 자연스럽게 정리하면서 상체에 시선이 가도록 균형을 맞췄습니다."
        bottom = "어두운 컬러의 스트레이트 팬츠"

    elif body_type == "마른 체형":
        body_reason = "전체적인 실루엣에 적당한 볼륨감을 더해 균형 잡힌 스타일을 연출했습니다."
        top = "니트 또는 여유 있는 셔츠"
        bottom = "와이드 팬츠"

    elif body_type == "전체적으로 균형 잡힌 체형":
        body_reason = "전체적으로 균형이 좋은 체형이므로 다양한 실루엣을 활용할 수 있습니다."

    else:
        body_reason = "기본적인 실루엣을 중심으로 누구나 쉽게 활용할 수 있는 코디를 추천했습니다."

    # 상황에 따른 수정
    if occasion == "면접":
        top = "화이트 셔츠"
        bottom = "네이비 또는 블랙 테일러드 슬랙스"
        shoes = "깔끔한 로퍼"
        accessory = "심플한 시계"

    elif occasion == "데이트":
        if style == "페미닌":
            top = "부드러운 컬러의 블라우스"
            bottom = "A라인 또는 플레어 스커트"
        else:
            top = "깔끔한 셔츠 또는 니트"
            bottom = "핏이 좋은 데님"
        shoes = "깔끔한 로퍼 또는 스니커즈"

    elif occasion == "학교":
        shoes = "편안한 스니커즈"

    elif occasion == "친구와의 약속":
        shoes = "캐주얼 스니커즈"

    elif occasion == "특별한 날":
        shoes = "로퍼 또는 깔끔한 플랫슈즈"

    # 색상에 따른 설명
    color_reason = ""

    if color == "블랙":
        color_reason = "블랙을 중심으로 구성해 세련되고 안정적인 분위기를 만들었습니다."
    elif color == "화이트":
        color_reason = "화이트를 활용해 깔끔하고 밝은 이미지를 강조했습니다."
    elif color == "네이비":
        color_reason = "네이비를 활용해 차분하면서도 세련된 분위기를 연출했습니다."
    elif color == "베이지":
        color_reason = "베이지 계열을 활용해 부드럽고 편안한 느낌을 강조했습니다."
    elif color == "브라운":
        color_reason = "브라운 계열을 활용해 따뜻하고 차분한 분위기를 만들었습니다."
    elif color == "파스텔":
        color_reason = "파스텔 컬러를 활용해 부드럽고 산뜻한 이미지를 연출했습니다."
    else:
        color_reason = "전체적인 색상 조화를 고려해 자연스럽게 매치할 수 있는 색상을 추천했습니다."

    return top, bottom, shoes, accessory, body_reason, color_reason


# --------------------------------------------------
# 추천 버튼
# --------------------------------------------------

st.markdown("---")

if st.button("✨ 나에게 맞는 코디 추천받기", use_container_width=True):

    if (
        gender == "선택해주세요"
        or body_type == "선택해주세요"
        or style == "선택해주세요"
        or color == "선택해주세요"
        or occasion == "선택해주세요"
    ):
        st.warning("모든 항목을 선택해주세요!")

    else:

        top, bottom, shoes, accessory, body_reason, color_reason = recommend_outfit(
            gender,
            body_type,
            style,
            color,
            occasion
        )

        st.markdown("## ✨ 당신을 위한 추천 코디")

        st.markdown(
            f"""
            <div class="result-box">

            <h3>👗 추천 스타일</h3>
            <p>
            <b>{style}</b> 스타일을 기반으로
            <b>{occasion}</b>에 어울리는 코디를 구성했습니다.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        # 의류 카드
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"""
                <div class="outfit-item">
                    <div class="item-title">TOP</div>
                    <div class="item-content">👕 {top}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="outfit-item">
                    <div class="item-title">BOTTOM</div>
                    <div class="item-content">👖 {bottom}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        col3, col4 = st.columns(2)

        with col3:
            st.markdown(
                f"""
                <div class="outfit-item">
                    <div class="item-title">SHOES</div>
                    <div class="item-content">👟 {shoes}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col4:
            st.markdown(
                f"""
                <div class="outfit-item">
                    <div class="item-title">ACCESSORY</div>
                    <div class="item-content">👜 {accessory}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # 추천 이유
        st.markdown("### 💡 AI 스타일링 분석")

        st.markdown(
            f"""
            <div class="reason">
            <b>체형 분석</b><br>
            {body_reason}
            <br><br>

            <b>컬러 분석</b><br>
            {color_reason}
            <br><br>

            <b>스타일 분석</b><br>
            {style} 스타일과 {occasion}이라는 상황을 고려하여
            실용성과 스타일을 함께 만족할 수 있도록 코디했습니다.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success("✨ 당신만의 스타일링이 완성되었습니다!")
