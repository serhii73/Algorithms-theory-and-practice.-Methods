def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        our_numbers = []
        our_numbers.append(a)
        our_numbers.append(b)
        a = max(our_numbers)
        b = min(our_numbers)
        while b !=0:
            numbers = []
            a = a % b
            numbers.append(a)
            numbers.append(b)
            a = max(numbers)
            b = min(numbers)
        return a

# a = 3918848
# b = 1653264


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()