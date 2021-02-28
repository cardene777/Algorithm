from typing import List


# ２部探索
def binary_search(data: List[int], value: int) -> int:
    data.sort()  # データのソート
    end = len(data) - 1  # data範囲の末尾
    start = 0  # data範囲の先頭
    while end >= start:
        median = (start + end) // 2  # data範囲の半分
        if data[median] == value:
            return median
        elif data[median] < value:
            start = median + 1
        else:
            end = median - 1
    return -1


if __name__ == '__main__':
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(binary_search(data, 10))
