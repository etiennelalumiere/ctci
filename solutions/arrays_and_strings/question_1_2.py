def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    char_counts = {}

    for i in range(len(str1)):
        current_char = str1[i]
        if str1 not in char_counts:
            char_counts[current_char] = 1
        else:
            char_counts[current_char] += 1

    for i in range(len(str2)):
        current_char = str2[i]
        if current_char not in char_counts:
            return False
        else:
            char_counts[current_char] -= 1
            if char_counts[current_char] < 0:
                return False

    return True


def main():
    print(is_permutation("abcd", "dcba"))
    print(is_permutation("abcd", "abc"))
    print(is_permutation("abcd", "abce"))


if __name__ == '__main__':
    main()