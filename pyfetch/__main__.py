import argparse

from pyfetch.fetch import Fetcher

# Fetcher.fetch()

def parse_args():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument(
        '-f',
        "--file_path",
        type=str,
        help="Request filepath of type .yaml , .yml or .json"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print(args)

if __name__ == "__main__":
    main()    