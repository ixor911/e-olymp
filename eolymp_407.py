def masha(flowers):
    buffer = flowers[1]
    flowers[1] = flowers[2]
    flowers[2] = buffer
    return flowers


def tanya(flowers):
    buffer = flowers[1]
    flowers[1] = flowers[0]
    flowers[0] = buffer
    return flowers


def show_flowers(flowers):
    print(flowers[0], flowers[1], flowers[2], sep='')


def start():
    amount_tests = int(input())
    for i in range(0, amount_tests):
        days = int(input())
        flowers = ['G', 'C', 'V']
        for j in range(0, days):
            flowers = masha(flowers)
            flowers = tanya(flowers)

        show_flowers(flowers)





