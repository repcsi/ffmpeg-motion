import ffmpeg


def convert(inFile):
    basename, extension = inFile.split(".")
    outFile = basename+"-temp."+extension
    ffmpeg.input(inFile).output(outFile, pix_fmt="yuv420p",vcodec="libx264",crf="20").run()
