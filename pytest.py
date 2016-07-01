import time
import io

def follow(file):
    file.seek(0, 0)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open('/dev/input/event4', buffering = -1, encoding =('latin-1'))
    loglines =  follow(logfile)
    for line in loglines:
        print (line)
