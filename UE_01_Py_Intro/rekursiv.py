__author__ = "Andrija Pavlovic"


def M(n):
    if n > 100:
        return n - 10
    else:
        return M(M(n + 11))


if __name__ == "__main__":
    print(M(99))
    print(M(100), '\n')

    m_list = []
    for n in range(200):
        m_list.append(M(n))
    print(m_list)
