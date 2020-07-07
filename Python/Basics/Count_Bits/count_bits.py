'''

Write a function that takes an integer as input,
and returns the number of bits that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010,
so the function should return 5 in this case

'''

def countBits(n):
    return bin(n)[2:].count('1')

def test_countBits():
    assert countBits(0) ==  0
    assert countBits(4) ==  1
    assert countBits(7) ==  3
    assert countBits(9) ==  2
    assert countBits(10) == 2