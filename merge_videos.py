import cv2
import os

def merge_videos_side_by_side(input_video, output_video, result_video):
    # Check if input files exist
    if not os.path.exists(input_video):
        print(f"Error: Input video file '{input_video}' does not exist.")
        return
    if not os.path.exists(output_video):
        print(f"Error: Output video file '{output_video}' does not exist.")
        return
    
    # Open the two video files
    cap1 = cv2.VideoCapture(input_video)
    cap2 = cv2.VideoCapture(output_video)
    
    # Check if each video opened successfully
    if not cap1.isOpened():
        print(f"Error: Could not open input video file '{input_video}'.")
        return
    if not cap2.isOpened():
        print(f"Error: Could not open output video file '{output_video}'.")
        return

    # Get properties of the videos
    width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap1.get(cv2.CAP_PROP_FPS))

    # Define codec and create VideoWriter for the output video
    output_width = width1 + width2
    output_height = max(height1, height2)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(result_video, fourcc, fps, (output_width, output_height))

    print("Starting to merge videos side by side...")

    while True:
        # Read frames from both videos
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        # If any of the frames couldn't be read, break the loop
        if not ret1 or not ret2:
            print("End of one or both videos reached.")
            break

        # Resize frames to the same height if needed
        if height1 != height2:
            frame1 = cv2.resize(frame1, (width1, output_height))
            frame2 = cv2.resize(frame2, (width2, output_height))

        # Concatenate frames horizontally
        merged_frame = cv2.hconcat([frame1, frame2])

        # Write the concatenated frame to the output video
        out.write(merged_frame)

    # Release resources
    cap1.release()
    cap2.release()
    out.release()
    print("Video merging complete. Saved as:", result_video)

if __name__ == "__main__":
    input_video = "sample_video/sony_A6300_4K.mp4"
    output_video = "sample_video/output_folder/output_sony_A6300_4K.mp4/output_sony_A6300_4K.mp4"
    result_video = "sample_video/merged_folder/merged_sony_A6300_4K.mp4"
    
    merge_videos_side_by_side(input_video, output_video, result_video)
