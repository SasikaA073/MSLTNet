import cv2
import os
import torch
import torchvision
from torchvision import transforms
from pyramid_structure.Omi_LP import MSLT
from torch.utils.data import DataLoader
import dataset.loaddata as loaddata
from merge_videos import merge_videos_side_by_side

def process_video(video_name, video_path, output_folder, model_path):
    print("Starting video processing...")

    # Create output folders
    frames_folder = os.path.join(output_folder, "frames")
    results_folder = os.path.join(output_folder, "results")
    os.makedirs(frames_folder, exist_ok=True)
    os.makedirs(results_folder, exist_ok=True)
    print("Output folders created.")

    # Load the video
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Video loaded. FPS: {fps}, Total frames: {frame_count}")

    # Split the video into frames
    print("Splitting video into frames...")
    frame_paths = []
    for i in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(frames_folder, f"frame_{i:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_paths.append(frame_path)
        if (i + 1) % 100 == 0:
            print(f"Processed {i + 1}/{frame_count} frames")

    cap.release()
    print("Video split into frames completed.")

    # Load and prepare the model
    print("Loading and preparing the model...")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = MSLT().to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    print(f"Model loaded and prepared. Using device: {device}")

    # Prepare data transforms
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])

    # Process the frames using the model
    print("Processing frames using the model...")
    with torch.no_grad():
        for i, frame_path in enumerate(frame_paths):
            # Load and preprocess the frame
            frame = cv2.imread(frame_path)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_tensor = transform(frame).unsqueeze(0).to(device)

            # Process the frame
            output = model(frame_tensor)

            # Save the result
            result_path = os.path.join(results_folder, f"result_{i:04d}.jpg")
            torchvision.utils.save_image(output, result_path)

            if (i + 1) % 100 == 0:
                print(f"Processed {i + 1}/{len(frame_paths)} frames")

    print("Frame processing completed.")

    # Convert the frames back to video
    print("Converting processed frames back to video...")
    video_name = video_name.split(".")[0]
    output_video_path = os.path.join(output_folder, f"output_{video_name}.mp4")
    frame = cv2.imread(os.path.join(results_folder, "result_0000.jpg"))
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for i in range(frame_count):
        result_path = os.path.join(results_folder, f"result_{i:04d}.jpg")
        frame = cv2.imread(result_path)
        out.write(frame)
        if (i + 1) % 100 == 0:
            print(f"Added {i + 1}/{frame_count} frames to video")

    out.release()
    print("Video conversion completed.")

    print(f"Video processing complete. Output saved to {output_video_path}")

if __name__ == "__main__":

    video_files = [file for file in os.listdir("./sample_video") if file.endswith((".mp4", ".avi", ".mov", ".flv", ".mpeg", ".mpg", ".wmv", ".webm", ".mkv"))]

    print("Available video files:")
    for i, file in enumerate(video_files):
        print(f"{i + 1}. {file}")

    video_index = int(input("Enter the index of the video file you want to process: "))
    video_name = video_files[video_index - 1]

    video_path = os.path.join("sample_video", video_name)
    output_folder = os.path.join("sample_video/output_folder", f"output_{video_name}")
    os.makedirs(output_folder, exist_ok=True)
    
    model_path = "pretrained_model/mslt+.pth"
    # process_video(video_name, video_path, output_folder, model_path)

    # Merge the input and output videos side by side
    [video_name, video_ftype] = video_name.split(".")

    input_video_path = video_path

    output_video_path = os.path.join(output_folder, f"output_{video_name}.{video_ftype}")

    merged_video_dir = "sample_video/merged_folder"
    merged_video_path = os.path.join(merged_video_dir, f"merged_{video_name}.{video_ftype}")

    merge_videos_side_by_side(input_video_path, output_video_path, merged_video_path)