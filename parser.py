import ffmpeg
import sys


def parseFile(fileName):
    try:
        probe = ffmpeg.probe(fileName)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        if video_stream is None:
            print('No video stream found', file=sys.stderr)
            sys.exit(1)
        return video_stream
    except ffmpeg.Error as e:
        print("exception!")
        print(e.stderr, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    videoFileName = "/motion/front1-20191011164740.mp4"
    videoStream = parseFile(videoFileName)
    print(f"codec name is: {videoStream['codec_name']}")



