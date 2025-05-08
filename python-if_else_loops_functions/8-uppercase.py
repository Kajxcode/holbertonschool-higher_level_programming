#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print(chr(ord(char) - 32) if ord(char) >= 97 and ord(char) <= 122 else char, end="")
