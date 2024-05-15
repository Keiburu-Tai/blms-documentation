import streamlit as st
import requests

# Streamlit 앱 헤더
st.title("MIDI 파일 업로드 및 재생기")

# FastAPI 서버 URL 설정
api_url = "http://localhost:8000"

# MIDI 파일 업로드
uploaded_file1 = st.file_uploader("첫 번째 MIDI 파일을 업로드하세요", type=["mid", "midi"], key="file_uploader1")
uploaded_file2 = st.file_uploader("두 번째 MIDI 파일을 업로드하세요", type=["mid", "midi"], key="file_uploader2")

# 볼륨 슬라이더
volume = st.slider("볼륨", 0.0, 1.0, 0.5)

# 파일을 FastAPI 서버에 전송하여 재생 요청하는 함수
def send_file_to_api(file, endpoint):
    files = {'file': (file.name, file, 'application/octet-stream')}
    data = {'volume': volume}
    response = requests.post(f"{api_url}/{endpoint}", files=files, data=data)
    return response

# 첫 번째 파일을 피아노로 재생
if uploaded_file1 is not None:
    response = send_file_to_api(uploaded_file1, "piano")
    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("파일 재생에 실패했습니다.")

# 두 번째 파일을 기타로 재생
if uploaded_file2 is not None:
    response = send_file_to_api(uploaded_file2, "guitar")
    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("파일 재생에 실패했습니다.")

st.write("Pygame을 종료하려면 웹 앱을 종료하세요.")
