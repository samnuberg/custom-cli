# Created by Sam Nuberg at 24/04/2021 17:48
import sys


def main():
    print('in main')
    args = sys.argv[1:]
    print(f'count of args :: {format(len(args))}')
    for arg in args:
        print(f'passed argument :: {format(arg)}')


if __name__ == '__main__':
    main()
