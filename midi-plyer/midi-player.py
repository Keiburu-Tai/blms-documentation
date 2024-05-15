import streamlit as st
import pygame
import multiprocessing
import tempfile
import time
import os

# Pygame 초기화 함수
def init_pygame():
    pygame.init()
    pygame.mixer.init()

# MIDI 파일 재생 함수
def play_midi_file(midi_filename, volume):
    init_pygame()
    pygame.mixer.music.set_volume(volume)
    try:
        pygame.mixer.music.load(midi_filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except pygame.error as e:
        print(f"파일을 재생하는 동안 오류가 발생했습니다: {e}")

# Streamlit 앱 헤더
st.title("MIDI 파일 독립적 재생기")

# MIDI 파일 업로드
uploaded_file1 = st.file_uploader("첫 번째 MIDI 파일을 업로드하세요", type=["mid", "midi"], key="file_uploader1")
uploaded_file2 = st.file_uploader("두 번째 MIDI 파일을 업로드하세요", type=["mid", "midi"], key="file_uploader2")

# 볼륨 슬라이더
volume = st.slider("볼륨", 0.0, 1.0, 0.5)

# 파일이 업로드되었는지 확인하고 독립적으로 재생
if uploaded_file1 is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mid') as tmp_file1:
        tmp_file1.write(uploaded_file1.read())
        midi_filename1 = tmp_file1.name
        st.text(f"{uploaded_file1.name} 파일이 재생됩니다.")
        p1 = multiprocessing.Process(target=play_midi_file, args=(midi_filename1, volume))
        p1.start()

if uploaded_file2 is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mid') as tmp_file2:
        tmp_file2.write(uploaded_file2.read())
        midi_filename2 = tmp_file2.name
        st.text(f"{uploaded_file2.name} 파일이 재생됩니다.")
        p2 = multiprocessing.Process(target=play_midi_file, args=(midi_filename2, volume))
        p2.start()

st.write("Pygame을 종료하려면 웹 앱을 종료하세요.")
