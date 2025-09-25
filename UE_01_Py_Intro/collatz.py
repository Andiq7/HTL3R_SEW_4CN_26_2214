from typing import List, Tuple

__author__ = "Andrija Pavlovic"


def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        print(n)


def collatz_sequence(number: int) -> List[int]:
    if number == 1:
        return [1]
    elif number == 4:
        return [4, 2, 1]
    elif number % 2 == 0:
        return [number] + collatz_sequence(number // 2)
    else:
        return [number] + collatz_sequence(3 * number + 1)

def collatz_length(number: int) -> int:
    return len(collatz_sequence(number))

def longest_collatz_sequence(n: int) -> Tuple[int, int]:
    """
       :param n: maximale Startzahl
       :return: (Startwert, Länge der längsten Collatz-Folge bis n)
       >>> longest_collatz_sequence(100)
       (97, 119)
       """
    max_length = 0
    best_start = 1
    for k in range(1, n + 1):
        length = collatz_length(k)
        if length > max_length:
            max_length = length
            best_start = k

    return best_start, max_length

if __name__ == "__main__":
    collatz(10)
    print()
    collatz(100)
    print()
    print(collatz_sequence(100), '\n')
    print(collatz_sequence(19), '\n')
    print(collatz_sequence(97), '\n')
    print(collatz_length(19), '\n')
    print(longest_collatz_sequence(100), '\n')

