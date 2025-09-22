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


def is_palindrome_sentence(s: str):
    """
    Prüft, ob der übergebene Satz ein Palindrom ist.

    Satzzeichen, Leerzeichen und Groß-/Kleinschreibung werden ignoriert.

    Beispiele:
    >>> is_palindrome_sentence("Eine güldne, gute Tugend: Lüge nie!")
    True
    >>> is_palindrome_sentence("Das ist kein Palindrom.")
    False
    >>> is_palindrome_sentence("Reliefpfeiler")
    True
    >>> is_palindrome_sentence("Otto liebt Anna")
    False
    >>> is_palindrome_sentence("A man, a plan, a canal: Panama")
    True
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
