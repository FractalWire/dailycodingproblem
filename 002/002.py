from typing import List
from collections import deque


def product_list_div(L: List[int]) -> List[int]:
    count0 = 0
    prod = 1

    for i in L:
        if i != 0:
            prod *= i
        else:
            count0 += 1
            if count0 > 1:
                return [0 for _ in L]

    if count0 == 1:
        return [prod if i == 0 else 0 for i in L]

    return [prod/i for i in L]


def product_list(L: List[int]) -> List[int]:
    left_prod_list, right_prod_list = list(), deque()
    prod_left, prod_right = 1, 1
    for i in range(len(L)):
        left_prod_list.append(prod_left)
        prod_left *= L[i]
        right_prod_list.appendleft(prod_right)
        prod_right *= L[-(i+1)]

    return [left_prod_list[i]*right_prod_list[i] for i in range(len(L))]


def main() -> None:
    assert product_list_div([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_list_div([3, 2, 1]) == [2, 3, 6]
    assert product_list_div([1, 0]) == [0, 1]
    assert product_list_div([1, 1, 0]) == [0, 0, 1]
    assert product_list_div([1, 0, 0]) == [0, 0, 0]

    assert product_list([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_list([3, 2, 1]) == [2, 3, 6]
    assert product_list([1, 0]) == [0, 1]
    assert product_list([1, 1, 0]) == [0, 0, 1]
    assert product_list([1, 0, 0]) == [0, 0, 0]

    print("all is good !")


if __name__ == "__main__":
    main()
