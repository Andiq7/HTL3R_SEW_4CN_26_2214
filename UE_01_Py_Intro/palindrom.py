__author__ = "Andrija Pavlovic"


def is_palindrom(s: str):
    """
    Prüft, ob der übergebene String ein Palindrom ist.

    Ein Palindrom liest sich von vorne und hinten gleich.

    Beispiele:
    >>> is_palindrom("otto")
    True
    >>> is_palindrom("anna")
    True
    >>> is_palindrom("python")
    False
    >>> is_palindrom("")
    True
    >>> is_palindrom("a")
    True
    """
    return s == s[::-1]


def is_palindrom_sentence(s: str):
    """
    Prüft, ob der übergebene Satz ein Palindrom ist.

    Satzzeichen, Leerzeichen und Groß-/Kleinschreibung werden ignoriert.

    Beispiele:
    >>> is_palindrom_sentence("Eine güldne, gute Tugend: Lüge nie!")
    True
    >>> is_palindrom_sentence("Das ist kein Palindrom.")
    False
    >>> is_palindrom_sentence("Reliefpfeiler")
    True
    >>> is_palindrom_sentence("Otto liebt Anna")
    False
    >>> is_palindrom_sentence("A man, a plan, a canal: Panama")
    True
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def palindrom_product(x: int):
        """
        Gibt das größte Palindrom zurück, das kleiner als x ist und als Produkt zweier dreistelliger Zahlen entsteht.

        Beispiele:
        >>> palindrom_product(101110)
        101101
        >>> palindrom_product(800000)
        793397
        >>> palindrom_product(10000)
        -1
        """
        max_pal = -1
        for a in range(100, 1000):
            for b in range(a, 1000):
                prod = a * b
                if prod < x and is_palindrom(str(prod)) and prod > max_pal:
                    max_pal = prod
        return max_pal

def to_base(number:int, base:int)->str:
    if base < 2 or base > 36:
        raise ValueError("Basis muss zwischen 2 und 36 liegen")

    if number == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    n = number
    while n > 0:
        n, remainder = divmod(n, base)
        result = digits[remainder] + result

    return result

def get_dec_hex_palindrom(x):
    if x <= 1:
        return -1

    for n in range(x - 1, -1, -1):
        if not is_palindrom(str(n)):
            continue
        hex_repr = to_base(n, 16)  # hier wird deine to_base Methode genutzt
        if hex_repr == hex_repr[::-1]:
            return n
    return -1

print(get_dec_hex_palindrom(1000))     # 979
print(get_dec_hex_palindrom(10000))    # 3003
print(get_dec_hex_palindrom(100000))   # 98689
print(get_dec_hex_palindrom(1))        # -1
