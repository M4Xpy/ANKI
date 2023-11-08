import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
import pyaudio
import wave
import time

def record_screen_and_audio(filename, duration):
    # Set up audio recording
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,  frames_per_buffer=1024)

    # Set up video recording
    screen = gw.getWindowsWithTitle(gw.getActiveWindowTitle())[0]
    screen_width, screen_height = screen.width, screen.height
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Adjust frame rate here (match with desired output frame rate)
    out = cv2.VideoWriter(filename, fourcc, 10.777, (screen_width, screen_height))  ##### 20.0

    # Record audio and video simultaneously
    frames = []
    audio_frames = []
    start = time.time()
    while time.time() < start + duration:
        frame = np.array(pyautogui.screenshot(region=(screen.left, screen.top, screen_width, screen_height)))
        frames.append(frame)
        audio_frame = stream.read(duration * 256)
        audio_frames.append(audio_frame)
        out.write(frame)
    print(time.time() - start)

    # Save audio as .wav file
    audio_file = wave.open(filename.removesuffix(".avi") + ".wav", 'wb')
    audio_file.setnchannels(1)
    audio_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    audio_file.setframerate(44100)
    audio_file.writeframes(b''.join(audio_frames))
    audio_file.close()

    # Release resources
    stream.stop_stream()
    stream.close()
    audio.terminate()
    out.release()

# import time
# time.sleep(9)
# Usage example:
file_address = f"C:\\ANKIsentences\\screen_recorder\\output_video.avi"
vaw = f"C:\\ANKIsentences\\screen_recorder\\output_video.wav"
record_screen_and_audio(file_address, 4)  # Record for 3 seconds

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

def get_media_duration(file_address):


    clip = VideoFileClip(file_address)
    duration = clip.duration
    clip.close()

    return duration

print(f".avi  =  {get_media_duration(file_address)}")
# print(f".wav  =  {get_media_duration(vaw)}")