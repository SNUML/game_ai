import sys
import argparse
import shutil
import os

def main(argv) :
    parser = argparse.ArgumentParser(description="Black and White Simulator")
    parser.add_argument('-f',dest='files',nargs='*',
        help="path of codes to run (at most 2)")
    parser.add_argument('-c',dest='count',nargs=1,type=int,default=[100],
        help="number of plays")
    parsed = parser.parse_args(argv[1:])

    if parsed.files != None :
        if len(parsed.files) > 2 :
            print("too many files! should be up to 2 files.")
            sys.exit()
        for i, path in enumerate(parsed.files) :
            shutil.copyfile(path,"src/player{}.py".format(i+1))

    os.system("python ./src/main.py {}".format(parsed.count[0]))
    
if __name__ == "__main__" :
    main(sys.argv)