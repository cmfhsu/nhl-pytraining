#!/usr/bin/env python
import sys
import os
import argparse

def main():
    args = parse_arguments()
    delete_files(args)

def parse_arguments():
    arg_parser = argparse.ArgumentParser(description="Delete all but newest files")

    arg_parser.add_argument(
        'startdir', help='Directory to search'
    )

    arg_parser.add_argument(
        'extension', help='Extension for files to delete'
    )

    arg_parser.add_argument(
        'numtokeep', help='Number of files to keep', type=int
    )


    return arg_parser.parse_args()


def delete_files(args):

    file_names = ( f for f in os.listdir(args.startdir) if f.endswith('.' + args.extension) )

    file_paths = ( os.path.join(args.startdir,f) for f in file_names )

    files = [ (f, os.path.getmtime(f)) for f in file_paths ]

    files.sort(key=lambda e: (e[1],e[0]),reverse=True)

    for file_path, file_timestamp in files[args.numtokeep:]:
        print("Deleting", file_path)  # for debugging
        # os.unlink(file_info[0])  # uncomment to actually delete

if __name__ == '__main__':
    main()
