__author__ = "Andrija Pavlovic"

def M(n):
    if n > 100:
        return n - 10
    else:
        return M(M(n + 11))

if __name__ == "__main__":
    print(M(99))
    print(M(100), '\n')
