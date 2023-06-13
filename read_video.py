import cv2
import numpy as np


def fun_one(video_path, frame_index):
    cap = cv2.VideoCapture(video_path)
    for i in range(frame_index+1):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 480))
        # 显示图像
        if i == frame_index:
            return frame


def fun_two(video_path, frame_index):
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))

    return frame


if __name__ == "__main__":
    # 打开视频文件
    video_path = "E:/对比影片运动轨/修正下载/downTool/downTool/store/28fedb11b53d679a.mp4"
    index = 500
    frame_one = fun_one(video_path, index)
    frame_two = fun_two(video_path, index)
    print(f"distance:{np.linalg.norm(frame_one - frame_two)}")

    cv2.imshow("one", frame_one)
    cv2.imshow("two", frame_two)
    cv2.waitKey(0)
