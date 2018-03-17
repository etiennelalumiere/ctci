def is_one_edit_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    else:
        if len(s1) == len(s2):
            return has_at_most_one_different_char(s1, s2)
        else:
            return has_at_most_one_extra_char(s1, s2)


def has_at_most_one_different_char(s1, s2):
    difference = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            difference += 1
            if difference > 1:
                return False

    return True


def has_at_most_one_extra_char(s1, s2):
    longest, shortest = find_longest_and_shortest(s1, s2)
    difference = 0

    for i in range(len(shortest)):
        if longest[i + difference] != shortest[i]:
            difference += 1
            if difference > 1:
                return False

    return True


def find_longest_and_shortest(s1, s2):
    if len(s1) > len(s2):
        return s1, s2
    else:
        return s2, s1


def main():
    print(is_one_edit_away('pale', 'ple'))
    print(is_one_edit_away('pales', 'pale'))
    print(is_one_edit_away('pale', 'bale'))
    print(is_one_edit_away('pales', 'bake'))


if __name__ == '__main__':
    main()