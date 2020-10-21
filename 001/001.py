from typing import List, Set


def isk_in_two(k: int, l: List[int]) -> bool:
    s: Set[int] = set()
    for i in l:
        if k-i in s:
            return True
        s.add(i)
    return False


def main():
    # simple example
    assert isk_in_two(17, [10, 15, 3, 7])
    # only two numbers
    assert isk_in_two(3, [1, 2])

    # simple example not in l
    assert not isk_in_two(1, [1, 2])
    # only one number
    assert not isk_in_two(1, [1])

    print("all is good !")


if __name__ == "__main__":
    main()
