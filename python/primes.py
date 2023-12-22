"""Module for dealing with primes"""
from typing import Generator


def new_prime() -> Generator[int, None, None]:
    """Generate Prime Numbers

    :yield Generator[int, None, None]: Prime Numbers
    """
    known_primes = [2]
    yield 2
    x=3
    while True:
        is_prime = True
        for known_prime in known_primes:
            is_prime = x % known_prime != 0 and is_prime
        if is_prime:
            known_primes.append(x)
            yield x
        x+=2

def first_n_primes(n:int)->list[int]:
    """Returns the first n primes

    :param int n: how many primes

    :return list[int]: list of primes
    """
    prime = new_prime()
    return [next(prime) for _ in range(n)]

def next_n_primes(x:int,n:int)->list[int]:
    """Returns the next n primes >x

    :param int x: input integer
    :param int n: how many primes
    :return list[int]: list of primes
    """
    prime = new_prime()
    while next(prime) <= x:
        pass
    return [next(prime) for _ in range(n)]

def next_prime(x:int)->int:
    """Returns the next prime > x

    :param int x: input integer
    :return int: the smallest prime greater than the input integer
    """
    prime = new_prime()
    while next(prime) <= x:
        pass
    return next(prime)


if __name__ == '__main__':
    print('Testing')
    print('---')
    print('First 10 primes:', first_n_primes(10))
    print('---')
    print(f"First prime > 100: {next_prime(100)}")
