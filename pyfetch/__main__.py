import argparse

from pyfetch.fetch import Fetcher

# Fetcher.fetch()

def parse_args():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument(
        '-f',
        "--request_file_path",
        type=str,
        help="Request file path of type .yaml , .yml or .json"
    )
    parser.add_argument(
        '-o',
        "--output_file_path",
        type=str,
        help="Output file path else prints to standard output."   
    )
    return parser.parse_args()


def main():
    args = parse_args()
    Fetcher.fetch(args.request_file_path,args.output_file_path)

if __name__ == "__main__":
    main()    