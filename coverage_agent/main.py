"""
Main file
"""
import argparse
from argparse import Namespace


def parse_args() -> Namespace:
    """
    Argument Parser
    """
    parser = argparse.ArgumentParser(description="Unit Test and Coverage"
                                     " Genarator",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--source_fp", "-s", type=str, required=True,
                        metavar='/a/src/code.py', help='Source code file path')
    parser.add_argument("--test_fp", "-t", type=str, required=True,
                        metavar='/a/test/test.py', help='Test code file path')
    parser.add_argument("--max_iters", "-m", type=int, required=False,
                        default=10, help='Maximum number of iterations')
    parser.add_argument("--version", "-v", type=str, required=False,
                        help='Library version')
    return parser.parse_args()


def main():
    """
    main function
    """
    args = parse_args()
    print(args)


if __name__ == "__main__":
    main()
