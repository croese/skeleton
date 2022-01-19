#!/usr/bin/env python3
import sys
import argparse
import pathlib


def extract_args(args):
    parser = argparse.ArgumentParser(
        description="Create a file tree from definition file",
    )
    parser.add_argument(
        "-r",
        "--root",
        help="Root directory to place the created file tree",
        type=pathlib.Path,
        default=".",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("name", nargs="?", help="Name of skel definition")
    group.add_argument("-f", "--file", help="Use specific skel file", type=pathlib.Path)

    return parser.parse_args(args)


def main():
    parsed = extract_args(sys.argv[1:])
    print(parsed)


if __name__ == "__main__":
    main()
