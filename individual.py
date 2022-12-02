#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set('abcdefghijklmnopqrstuvwxyz')

    a = {'b', 'c', 'g', 'I', 'w'}
    b = {'e', 'g', 'h', 'q', 'w'}
    c = {'c', 'd', 'k', 'l', 'y'}
    d = {'a', 'g', 'h', 'u', 'z'}

    x = (a.intersection(c)).union(b)
    print(f"x = {x}")

    an = u.difference(a)

    y = (an.intersection(d)).union(c.difference(b))

    print(f"y = {y}")