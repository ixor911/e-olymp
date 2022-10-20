import math


def time_difference(time_list1, time_list2):
    minutes = time_list2[1] - time_list1[1] + 60
    hours = time_list2[0] - time_list1[0] - 1
    hours += int(minutes / 60)
    hours = math.ceil(hours)
    minutes = math.ceil(minutes % 60)

    return [hours, minutes]
    # 1 50 -> 2 10 => 0 20
    # 1 20 -> 1 40 => 0 20


def start():
    a_send = input()
    b_receive = input()
    b_send = input()
    a_receive = input()

    a_send_l = list(map(int, a_send.split(':')))
    b_receive_l = list(map(int, b_receive.split(':')))
    b_send_l = list(map(int, b_send.split(':')))
    a_receive_l = list(map(int, a_receive.split(':')))

    a_b_diff = time_difference(a_send_l, b_receive_l)
    b_a_diff = time_difference(b_send_l, a_receive_l)

    ans = [int((a_b_diff[0] + b_a_diff[0]) / 2), int((a_b_diff[1] + b_a_diff[1]) / 2)]

    if ans[0] < 10:
        ans[0] = '0' + str(ans[0])
    if ans[1] < 10:
        ans[1] = '0' + str(ans[1])

    print(ans[0], ans[1], sep=':')


