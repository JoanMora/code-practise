def reverse_bits(n):
    def reverse_bits(n):
    # use the in-build python function to get the binary
    # bin(number) returns 0b or -0b to indicate the sign followed by the actual bin number
    binary_number = bin(n)[2:] #.zfill(8) here there is no need of filling
    # reverse the binary number
    bin_num_reversed = ''.join(reversed(binary_number))
    # get the integer number from a bin num
    reversed_decimal = int(bin_num_reversed,2)
