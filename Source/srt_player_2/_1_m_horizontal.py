from moviepy.editor import VideoFileClip, ColorClip, clips_array

def make_vertical_video(input_path, output_path, duration=60):
    # Load the video clip
    video_clip = VideoFileClip(input_path)


    # Determine the target width and height for the vertical video
    target_width = video_clip.size[0]  # Width becomes height
    target_height = video_clip.size[1]  # Height becomes width

    # Crop the video to the specified duration
    cropped_clip = video_clip.subclip(0, duration)

    # Create a blank clip to concatenate if the video duration is less than the specified duration
    blank_clip_duration = max(0, duration - cropped_clip.duration)
    blank_clip = ColorClip((target_width, target_height), color=(0, 0, 0), duration=blank_clip_duration)

    # Concatenate the cropped clip with the blank clip (if needed)
    vertical_clip = clips_array([[cropped_clip], [blank_clip]])

    # Write the result to the output file
    vertical_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Close the video clip objects
    video_clip.close()
    cropped_clip.close()
    blank_clip.close()
    vertical_clip.close()








# Example usage:
input_video_path = "C:\\Users\\Я\\Desktop\\ready video\\full\\hercules.avi"
output_video_path = "C:\\Users\\Я\\Desktop\\ready video\\full\\horizontal_video.mp4"

make_vertical_video(input_video_path, output_video_path, duration=5)
