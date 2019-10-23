import ffmpeg
import tempfile
import shutil

def convert(inFile):
    basename, extension = inFile.split(".")
    tmpFile = tempfile.mktemp()
    #outFile = basename+"-temp."+extension
    outFile = tmpFile
    ffmpeg.input(inFile).output(outFile, format="mp4", pix_fmt="yuv420p", vcodec="libx264", crf="20").run()
    shutil.move(outFile, inFile)
