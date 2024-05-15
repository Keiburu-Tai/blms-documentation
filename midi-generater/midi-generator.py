import mido
from mido import MidiFile, MidiTrack, Message

# 새로운 MIDI 파일 생성
mid = MidiFile()

# 멜로디 트랙 생성
melody_track = MidiTrack()
mid.tracks.append(melody_track)

# 템포 설정 (120 BPM)
tempo = mido.bpm2tempo(120)
melody_track.append(mido.MetaMessage('set_tempo', tempo=tempo))

# 프로그램 체인지 (멜로디: 피아노)
melody_track.append(Message('program_change', program=0))

# 멜로디 작성 (도, 레, 미, 파, 솔)
melody_notes = [60, 62, 64, 65, 67]  # MIDI 노트 번호 (C4, D4, E4, F4, G4)
for note in melody_notes:
    melody_track.append(Message('note_on', note=note, velocity=64, time=0))
    melody_track.append(Message('note_off', note=note, velocity=64, time=480))

# 베이스 트랙 생성
bass_track = MidiTrack()
mid.tracks.append(bass_track)

# 프로그램 체인지 (베이스: 어쿠스틱 베이스)
bass_track.append(Message('program_change', program=32))

# 베이스 작성 (C2, D2, E2, F2, G2)
bass_notes = [36, 38, 40, 41, 43]  # MIDI 노트 번호 (C2, D2, E2, F2, G2)
for note in bass_notes:
    bass_track.append(Message('note_on', note=note, velocity=64, time=0))
    bass_track.append(Message('note_off', note=note, velocity=64, time=480))

# 드럼 트랙 생성 (채널 10)
drum_track = MidiTrack()
mid.tracks.append(drum_track)

# 드럼 패턴 작성 (Kick, Snare, Hi-Hat)
drum_track.append(Message('program_change', program=0, channel=9))

# 드럼 노트 번호
kick = 36    # Bass Drum (C1)
snare = 38   # Acoustic Snare (D1)
hihat = 42   # Closed Hi-Hat (F#1)

# 패턴 반복
for _ in range(4):
    drum_track.append(Message('note_on', note=kick, velocity=64, time=0, channel=9))
    drum_track.append(Message('note_off', note=kick, velocity=64, time=240, channel=9))

    drum_track.append(Message('note_on', note=hihat, velocity=64, time=0, channel=9))
    drum_track.append(Message('note_off', note=hihat, velocity=64, time=240, channel=9))

    drum_track.append(Message('note_on', note=snare, velocity=64, time=0, channel=9))
    drum_track.append(Message('note_off', note=snare, velocity=64, time=240, channel=9))

    drum_track.append(Message('note_on', note=hihat, velocity=64, time=0, channel=9))
    drum_track.append(Message('note_off', note=hihat, velocity=64, time=240, channel=9))

# MIDI 파일 저장
mid.save('melody_bass_drums.mid')

print("MIDI 파일이 성공적으로 작성되었습니다: melody_bass_drums.mid")
