def start1():
    ans = int(input())
    second = ans % 10
    first = int((ans - second) / 10)
    print(f"{first} {second}")


