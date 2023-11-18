import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def join_avi_files_in_folder(folder_path, output_file):
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Filter only AVI files
    avi_files = [f for f in files if f.lower().endswith(".avi")]

    # Create a list of VideoFileClip objects from the AVI files
    video_clips = [VideoFileClip(os.path.join(folder_path, file)) for file in avi_files]

    # Concatenate the video clips
    final_clip = concatenate_videoclips(video_clips, method="compose")


    bitrate = "1500k"  # Adjust this value based on your desired file size and quality

    # Write the result to a new file with adjusted resolution and bitrate
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac",  bitrate=bitrate)




# Example usage:
folder_path = f"C:\\Users\\Я\\Documents\\Bandicam\\alice"
output_file = f"C:\\Users\\Я\\Documents\\Bandicam\\output_combined.avi"

join_avi_files_in_folder(folder_path, output_file)
