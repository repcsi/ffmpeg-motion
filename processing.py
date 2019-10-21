import os
import ffmpeg
import tempfile

def convert(inFile):
    basename, extension = inFile.split(".")
    tmpFile = tempfile.mktemp()
    #outFile = basename+"-temp."+extension
    outFile = tmpFile
    ffmpeg.input(inFile).output(outFile, pix_fmt="yuv420p",vcodec="libx264",crf="20").run()
    os.rename(outFile, inFile)
