import unittest
import os
from os import listdir, path
from pathlib import Path

class TestSwap(unittest.TestCase):
    def test_imports(self):
        from pytube import YouTube
    def test_get_video(self):
        from main import get_video
        rickroll = 'https://youtu.be/dQw4w9WgXcQ'
        video_path = get_video(rickroll)
        self.assertTrue(path.exists(video_path))
    def test_cut_video(self):
        from main import cut_video
        start = 30
        length = 10 
        vid_path = Path("C:/Users/ru1072781/Repo/yt-swap/video_in/Rick Astley - Never Gonna Give You Up (Video).mp4")
        cut_path = cut_video(vid_path, start, length)
        self.assertTrue(path.exists(cut_path))
    def test_swap_faces(self):
        from main import swap_faces
        vid_path = Path("C:/Users/ru1072781/Repo/yt-swap/cut_vid/Rick Astley - Never Gonna Give You Up (Video).mp4")
        im_path = Path("C:/Users/ru1072781/Repo/yt-swap/image_in/obama.png")
        final_path = swap_faces(vid_path, im_path)
        self.assertTrue(path.exists(final_path))
        




if __name__ == "__main__":
    unittest.main()