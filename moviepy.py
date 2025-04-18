from moviepy.editor import VideoFileClip, clips_array

# Load the frontal, left, and right videos
frontal = VideoFileClip("frontal.mp4")
left_view = VideoFileClip("left_view.mp4")
right_view = VideoFileClip("right_view.mp4")

# Combine the videos side by side
final_video = clips_array([[left_view, frontal, right_view]])
final_video.write_videofile("output.mp4", fps=24)
