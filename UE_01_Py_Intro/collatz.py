from typing import List, Tuple

__author__ = "Andrija Pavlovic"


def collatz(n):
    """
    Gibt die Collatz-Folge von n auf der Konsole aus.
    >>> collatz(6)
    3
    10
    5
    16
    8
    4
    2
    1
    """
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        print(n)

def collatz_sequence(number: int) -> List[int]:
    """
    Gibt die Collatz-Folge als Liste zurück.
    >>> collatz_sequence(6)
    [6, 3, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    if number == 1:
        return [1]
    elif number == 4:
        return [4, 2, 1]
    elif number % 2 == 0:
        return [number] + collatz_sequence(number // 2)
    else:
        return [number] + collatz_sequence(3 * number + 1)

def collatz_length(number: int) -> int:
    """
    Gibt die Länge der Collatz-Folge zurück.
    >>> collatz_length(6)
    9
    >>> collatz_length(19)
    21
    """
    return len(collatz_sequence(number))

def longest_collatz_sequence(n: int) -> Tuple[int, int]:
    """
    Gibt den Startwert und die Länge der längsten Collatz-Folge bis n zurück.
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

