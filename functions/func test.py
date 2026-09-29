def main():
    n = 10
    print(modsum(n))


def modsum(n):
    total = 0
    for i in range(n, 0, -1):
        value = i % 3
        total = total + value
    return total


main()