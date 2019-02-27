"""
https://en.wikipedia.org/wiki/RSA_(cryptosystem)
https://en.wikipedia.org/wiki/Carmichael_function
https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
https://gist.github.com/JonCooperWorks/5314103
"""

import random


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False


def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modular_multiplicative_inverse(e, lcm):
    g, x, y = egcd(e, lcm)
    if g != 1:
        raise Exception('Modular inverse does not exist.')
    else:
        return x % lcm


def key_gen(p, q):
    if p == q:
        raise Exception(f'{p} == {q}')
    elif not is_prime(p) or not is_prime(q):
        raise Exception(f'{p} or {q} is not prime')

    # Based on Wiki
    n = p * q

    # Calculating lamda(n) using Carmichael's totient function
    lcm = (p - 1) * (q - 1)
    e = random.randrange(1, lcm)
    gcd = greatest_common_divisor(e, lcm)
    while gcd != 1:
        e = random.randrange(1, lcm)
        gcd = greatest_common_divisor(e, lcm)

    d = modular_multiplicative_inverse(e, lcm)

    return (e, n), (d, n)


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]

    return cipher


def decrypt(pk, cipher):
    key, n = pk
    plain = [chr((char ** key) % n) for char in cipher]

    return ''.join(plain)


if __name__ == '__main__':
    prime1 = int(input('Input a prime number: '))
    prime2 = int(input('Input another different prime number: '))
    public, private = key_gen(p=prime1, q=prime2)
    print(f'Public key = {public}')
    print(f'Private key = {private}')

    text = input('Input a message: ')
    encrypted = encrypt(private, text)
    print(f'Encrypted message = {"".join([str(msg) for msg in encrypted])}')
    print(f'Decrypted message = {decrypt(public, encrypted)}')
