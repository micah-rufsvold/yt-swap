from pytube import YouTube
from pathlib import Path
import os
import argparse
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from FaceSwap.main_video import VideoHandler
class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def get_video(url : str) -> Path:
    vid_url = YouTube(url)
    down_folder = Path(os.path.dirname(__file__)) 
    res_dict = {"low":"240p",
                "medium":"360p",
                "high":"720p"}
                
    vid_options = vid_url.streams.filter(audio_codec = 'mp4a.40.2', type='video')
    vid = vid_options.first()
    vid_path = Path(vid.download(down_folder / 'video_in'))
    return vid_path

def cut_video(vid_path : Path, start_time : int, length = 15) -> Path:
    output =  Path('cut_vid/' + vid_path.name)
    ffmpeg_extract_subclip(vid_path, start_time, start_time+length, targetname=output)
    return Path(os.path.dirname(__file__)) / output

def swap_faces(vid_path : Path, im_path : Path) -> Path :
    out_path = Path('final/' + vid_path.name)
    args = Namespace(src_img = str(im_path), video_path=str(vid_path), correct_color = True, warp_2d=True,save_path=str(out_path), show=False)
    VideoHandler(args.video_path, args.src_img, args).start()
    return Path(os.path.dirname(__file__))/out_path

if __name__ == '__main__':
    pass

#add comment