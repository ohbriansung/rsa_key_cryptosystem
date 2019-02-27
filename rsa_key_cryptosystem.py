"""
https://en.wikipedia.org/wiki/RSA_(cryptosystem)
https://gist.github.com/JonCooperWorks/5314103
"""


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        return True
    return False


def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def key_gen(prime1, prime2):
    if prime1 == prime2:
        raise Exception(f"{prime1} == {prime2}")
    elif not is_prime(prime1) or not is_prime(prime2):
        raise Exception(f"{prime1} or {prime2} is not prime")


if __name__ == "__main__":
    prime1 = input("Input a prime number: ")
    prime2 = input("Input another different prime number: ")


