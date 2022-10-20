def start1():
    ans = input()
    print(len(ans))


def start():
    ans = int(input())
    amount = 0

    if ans == 0:
        print(1)

    while ans != 0:
        if pow(10, amount) > ans:
            print(amount)
            break

        amount += 1
