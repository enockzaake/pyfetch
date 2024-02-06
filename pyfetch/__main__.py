import argparse

from pyfetch.fetch import Fetcher

Fetcher.fetch()

def parse_args():
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument(
        '-f',
        "--file_path",
        type=str,
        help="Request filepath of type .yaml , .yml or .json"
    )
    return ap.parse_args()


def main():
    args = parse_args()
    