from gtts import gTTS
from moviepy.editor import AudioFileClip, TextClip, CompositeVideoClip
import os

def create_karaoke_video(text, output_file):
    # Convert text to speech
    tts = gTTS(text)
    tts.save("temp_audio.mp3")

    # Generate video
    audio = AudioFileClip("temp_audio.mp3")
    # txt_clip = TextClip(text, fontsize=70, color='white')
    # txt_clip = txt_clip.set_pos(('center', 'bottom')).set_duration(audio.duration)
    video = CompositeVideoClip([txt_clip.set_audio(audio)])
    video.write_videofile(output_file, audio_codec='aac')

    # Clean up temp files
    os.remove("temp_audio.mp3")


# Example usage:
create_karaoke_video("Hello, this is a karaoke video!", "karaoke_video.mp4")
