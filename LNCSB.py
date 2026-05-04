def longest_consecutive_ones(n):
    binary = bin(n)[2:]
    ones_sequences = binary.split('0')
    return max(len(seq) for seq in ones_sequences)

num = int(input("Enter a number: "))
print(longest_consecutive_ones(num))
