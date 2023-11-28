from moviepy.editor import VideoFileClip, clips_array

def make_vertical_video(input_path, output_path):
    # Load the video clip
    video_clip = VideoFileClip(input_path)

    # Rotate the video clip 90 degrees clockwise to make it vertical
    vertical_clip = video_clip.rotate(-90)

    # Write the result to the output file
    vertical_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Close the video clip objects
    video_clip.close()
    vertical_clip.close()

# Example usage:
input_video_path = "C:\\Users\\Я\\Desktop\\ready video\\bandicam 2023-11-28 17-41-54-169.mp4"
output_video_path = "C:\\Users\\Я\\Desktop\\ready video\\short.mp4"

make_vertical_video(input_video_path, output_video_path)
