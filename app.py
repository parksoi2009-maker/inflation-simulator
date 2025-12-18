import streamlit as st
import pandas as pd

st.title("📉 물가 변화 시뮬레이터")

# 입력
income = st.number_input("월 소득 (만원)", min_value=50, value=200)
inflation = st.slider("연 물가상승률 (%)", 0.0, 10.0, 3.0)
years = st.slider("시뮬레이션 기간 (년)", 1, 10, 5)

# 계산
data = []
for year in range(1, years + 1):
    real_income = income / ((1 + inflation / 100) ** year)
    data.append({
        "연도": year,
        "실질 소득 (만원)": round(real_income, 2)
    })

df = pd.DataFrame(data)

# 출력
st.subheader("📊 연도별 실질 소득 변화")
st.line_chart(df.set_index("연도"))

st.write(df)

st.info(
    f"{years}년 후 현재 가치로 보면 "
    f"월 소득 {income}만 원은 "
    f"약 {round(df.iloc[-1]['실질 소득 (만원)'], 1)}만 원의 가치입니다."
)
