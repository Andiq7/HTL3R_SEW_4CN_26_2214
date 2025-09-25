from time import time

__author__ = "Andrija Pavlovic"


def M(n):
    if n > 100:
        return n - 10
    else:
        return M(M(n + 11))


if __name__ == "__main__":
    print(M(99))
    print(M(100), '\n')

    t0 = time()
    m_list = []
    for n in range(200):
        m_list.append(M(n))
    print(m_list)
    t1 = time()
    print("Dauer Liste: ", t1 - t0, "Sekunden")

    t2 = time()
    m_dict = {}
    for n in range(200):
        m_dict[n] = M(n)
    print(m_dict)
    t3 = time()
    print("Dauer Dict: ", t3 - t2, "Sekunden")

    # Bemerkenswert an der Funktion M(n) (McCarthy-91-Funktion) ist, dass für
    # alle Werte von n ≤ 100 das Ergebnis immer 91 ist. Nur für Werte von n > 100
    # liefert die Funktion n - 10 zurück. Das zeigt, wie Rekursion zu einem konstanten
    # Ergebnis für einen großen Wertebereich führen kann.
