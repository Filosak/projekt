def is_prime(val):
    if val <= 1:
        return False
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            return False
    return True

def is_palindrome(string):
    reverse=string[::-1]
    for i in range(len(string)):
        if string[i]!=reverse[i]:
            print(string, " neni palindrom.")
            return;
    print(string, "je palindrom!!")


def is_vowel(char):
    vowels=["a","e","i","y","o","u"]
    if char in vowels:
        print(char, " je samohlaska.")
        return True;
    else:
        print(char, " neni samohlaska.")
        return False;

is_palindrome("krk")
is_palindrome("bludimir")
is_vowel("b")
is_vowel("e")