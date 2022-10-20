import math


def start():
    rooms = int(input())
    tin = 16
    for i in range(0, rooms):
        L, W, H = map(int, input().split())
        wall_a = L * H
        wall_b = W * H
        full = wall_b * 2 + wall_a * 2
        print(math.ceil(full/tin))




start()




