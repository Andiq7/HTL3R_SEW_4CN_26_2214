__author__ = "Andrija Pavlovic"


def is_palindrome(s: str):
        """
        Prüft, ob der übergebene String ein Palindrom ist.

        Ein Palindrom liest sich von vorne und hinten gleich.

        Beispiele:
        >>> is_palindrome("otto")
        True
        >>> is_palindrome("anna")
        True
        >>> is_palindrome("python")
        False
        >>> is_palindrome("")
        True
        >>> is_palindrome("a")
        True
        """
        return s == s[::-1]


if __name__ == "__main__":
    print("palindrom.py wurde direkt ausgeführt")
