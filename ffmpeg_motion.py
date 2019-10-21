from os import listdir
from os.path import join

import multiprocessing
import signal
import time
import yaml

# local stuff:
from parser import parseFile
from processing import convert

start = time.time()


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def readConfig():
    with open("config.yaml", 'r') as yamlfile:
        try:
            config = yaml.safe_load(yamlfile)
        except yaml.YAMLError as exc:
            print(exc)

    print("Config dump: ")
    for section in config:
        print(section + ":" + str(config[section]))
    return config


def readFilesInDir(directory):
    filestocheck = listdir(directory)
    # TODO: check if files are open and load them in this method!
    return filestocheck


if __name__ == '__main__':
    workList = []
    config = readConfig()
    workingDirectory = config['video_directory']
    fileType = config['filetype']
    fileList = readFilesInDir(workingDirectory)
    stream_type = config['streamtype']
    stream_attribute = config['stream_attribute']
    if ('processes' in config):
        processes = config['processes']
    else:
        processes = multiprocessing.cpu_count() - 1

    print(f"worker count: {processes}")

    for files in fileList:
        if (fileType in files):
            longFileName = join(workingDirectory, files)
            try:
                videoStream = parseFile(longFileName)
                #if (videoStream['codec_name'] == "hevc"):
                if (videoStream[stream_type] == stream_attribute):
                    workList.append(longFileName)
                    print("append!")
            except:
                continue


    print(f"workList length: {len(workList)} ")

    pool = multiprocessing.Pool(processes, initializer=init_worker)

    try:
        pool.map(convert, workList)
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating")
        pool.terminate()
        pool.join()

    print("Elapsed Time: %s seconds" % round((time.time() - start), 4))
    print("DONE!")
