def is_palindrome_permutation(phrase):
    bit_vector = create_bit_vetcor(phrase)
    return bit_vector == 0 or has_exactly_one_bit_set(bit_vector)


def create_bit_vetcor(phrase):
    phrase = phrase.replace(' ', '')
    bit_vector = 0

    for c in phrase:
        bit_vector = toggle(bit_vector, ord(c) - ord('a'))

    return bit_vector


def toggle(bit_vector, index):
    return bit_vector ^ (1 << index)


def has_exactly_one_bit_set(bit_vector):
    return (bit_vector & (bit_vector - 1)) == 0


def main():
    print(is_palindrome_permutation('taco cat'))
    print(is_palindrome_permutation('tacocat'))
    print(is_palindrome_permutation('taccat'))
    print(is_palindrome_permutation('ttaaccat'))


if __name__ == '__main__':
    main()