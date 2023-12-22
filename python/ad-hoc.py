from primes import next_n_primes
from morse import text_to_morse

for prime in next_n_primes(9213,10):
    print(prime, text_to_morse(str(prime)))