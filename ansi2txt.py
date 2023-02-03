#!/usr/bin/env python

# SPDX-License-Identifier: MIT AND AGPL-3.0-only

import sys


def getchar():
    return sys.stdin.buffer.read(1)


def putchar(c):
    return sys.stdout.buffer.write(c)


def main():
    EOF = b""
    ch = None

    while ch != EOF:
        ch = getchar()
        while ch == "\r":
            ch = getchar()
            if ch != "\n":
                putchar("\r")

        if ch == "\x1b":
            ch = getchar()
            if ch == "[":
                ch = getchar()
                while ch == ";" or (ch >= "0" and ch <= "9") or ch == "?":
                    ch = getchar()
            elif ch == "]":
                ch = getchar()
                if ord(ch) >= 0 and ch <= "9":
                    while True:
                        ch = getchar()
                        if ch == EOF or ord(ch) == 7:
                            break
                        elif ch == "\x1b":
                            ch = getchar()
                            break
            elif ch == "%":
                ch = getchar()
            else:
                pass
        elif ch != EOF:
            putchar(ch)


if __name__ == "__main__":
    main()
