
# Ulam Spirals

A python script which generates Ulam Spirals with each number having 
a different size based on how many factors it has.

The primes are indexed before hand using a modified sieve of Eratosthenes.
This is much faster than calculating the number of factors of each number individually,
allowing for making more detailed spirals.
## Usage

Install dependencies by running
```pip install -r requirements.txt```
from the root directory.

Run the program by
```
cd main
py main.py
```

## References

Sieve of Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes  
Ulam Spiral: https://en.wikipedia.org/wiki/Ulam_spiral  
Similar reddit post: https://www.reddit.com/r/dataisbeautiful/comments/1djjzv/different_ulam_spiral_all_numbers_from_1_to/