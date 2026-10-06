def is_prime(val):
    if val <= 1:
        return False
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            return False
    return True

def is_palindrome(string):
    pass