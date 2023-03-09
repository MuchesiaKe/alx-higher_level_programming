#!/usr/bin/python3
def pow(a, b):
    power = 1
    i = 0
    while (i < b):
        power = power * a
        i = i + 1
    return power
