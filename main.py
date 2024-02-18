import cv2
import os
import argparse
from tqdm import tqdm
import textwrap

def extract_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    # Create a tqdm progress bar
    pbar = tqdm(total=total_frames, desc='Extracting frames', unit='frame')

    # Iterate through the video frames
    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Annotate frame with image name and timestamp
        image_name = f"frame_{frame_number:05d}.jpg"

        # Calculate timestamp
        timestamp_seconds = frame_number / fps
        minutes = int(timestamp_seconds // 60)
        seconds = int(timestamp_seconds % 60)
        milliseconds = int((timestamp_seconds - int(timestamp_seconds)) * 1000)
        timestamp_text = f"{minutes:02d}:{seconds:02d}:{milliseconds:03d}"

        # Combine image name and timestamp with newline character
        text_to_display = "Image Name: {}\nTime: {}".format(image_name, timestamp_text)

        # Calculate text size
        text_size, _ = cv2.getTextSize(text_to_display, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

        # Calculate text position to center it inside the box
        text_x = 20  # left padding
        text_y = text_size[1] + 30  # top padding

        # Add semi-transparent box
        overlay = frame.copy()
        cv2.rectangle(overlay, (10, 10), (text_size[0] + 40, text_size[1] * 3 + 60), (0, 0, 0), -1)  # Black semi-transparent box

        # Add text on top of the box
        cv2.putText(overlay, text_to_display, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Combine the frame and overlay
        alpha = 0.5  # Opacity factor
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

        # Save the frame as an image
        frame_path = os.path.join(output_folder, image_name)
        cv2.imwrite(frame_path, frame)
        frame_number += 1
        pbar.update(1)

    pbar.close()
    cap.release()

def create_video(image_folder, output_video_path, fps, duration):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images.sort()

    # Define the codec and create VideoWriter object
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_video_path, fourcc, fps, (width,height))

    # Create a tqdm progress bar
    pbar = tqdm(total=len(images), desc='Creating video', unit='frame')

    # Write frames to the video
    for image in images:
        img_path = os.path.join(image_folder, image)
        frame = cv2.imread(img_path)

        # Get current frame number
        current_frame_number = int(image.split("_")[1].split(".")[0])

        # Write frame number on top left corner inside a gray box
        cv2.rectangle(frame, (0, 0), (150, 40), (128, 128, 128), -1)
        cv2.putText(frame, f"Frame: {current_frame_number}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        video.write(frame)
        pbar.update(1)

    pbar.close()
    cv2.destroyAllWindows()
    video.release()

def main():
    parser = argparse.ArgumentParser(description="Convert video into image frames and then generate a video from the frames.")
    parser.add_argument("video_path", help="Path to the input video file")
    parser.add_argument("output_path", help="Path to the output video file")
    parser.add_argument("image_folder", help="Path to the folder where image frames will be stored")
    args = parser.parse_args()

    video_path = args.video_path
    output_video_path = args.output_path
    image_folder = args.image_folder

    # Extract frames from the video
    extract_frames(video_path, image_folder)

    # Get video properties
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps
    cap.release()

    # Create video from frames
    create_video(image_folder, output_video_path, fps, duration)

if __name__ == "__main__":
    main()
