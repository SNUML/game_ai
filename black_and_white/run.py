import sys
import argparse
import shutil
import os

def main(argv) :
    parser = argparse.ArgumentParser(description="Black and White Simulator")
    parser.add_argument('-f',dest='files',nargs='*',
        help="Path of Codes to Run (should be .py)")
    parser.add_argument('-c',dest='count',nargs=1,type=int,default=100,
        help="Number of Plays")
    parsed = parser.parse_args(argv[1:])

    if parsed.files != None :
        if len(parsed.files) > 2 :
            print("Too Many Files")
            sys.exit()
        for i, path in enumerate(parsed.files) :
            shutil.copyfile(path,"src/player{}.py".format(i+1))

    os.system("python ./src/main.py {}".format(parsed.count))
    
if __name__ == "__main__" :
    main(sys.argv)