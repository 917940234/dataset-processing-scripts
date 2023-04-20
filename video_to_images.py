import cv2
import os

def extract_frames(video_path, output_folder, sample_rate):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    img_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % sample_rate == 0:
            img_name = os.path.join(output_folder, f"{img_count:04d}.png")
            cv2.imwrite(img_name, frame)
            img_count += 1

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()


def process_videos(videos_folder, output_folder, sample_rate):
    for file_name in os.listdir(videos_folder):
        if file_name.endswith(('.mp4', '.avi', '.mkv', '.mov', '.flv')):
            video_path = os.path.join(videos_folder, file_name)
            video_name = os.path.splitext(file_name)[0]
            video_output_folder = os.path.join(output_folder, video_name)

            # 创建视频对应的子文件夹
            if not os.path.exists(video_output_folder):
                os.makedirs(video_output_folder)

            extract_frames(video_path, video_output_folder, sample_rate)


if __name__ == "__main__":
    videos_folder = "C:\\Users\\91794\\Documents\\SyncSpace\\IdeaStorm\\PycharmProjects\\ScrapMind\\datasets\\video"
    output_folder = "C:\\Users\\91794\\Documents\\SyncSpace\\IdeaStorm\\PycharmProjects\\ScrapMind\\datasets\\images"
    sample_rate = 5

    process_videos(videos_folder, output_folder, sample_rate)
