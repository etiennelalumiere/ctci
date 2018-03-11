def has_unique_characters_1(string):
    string = sorted(string)

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True


def has_all_unique_characters_2(string):
    string = sorted(string)

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True


def main():
    print(has_unique_characters_1("aosidufy"))
    print(has_unique_characters_1("aosiadufy"))


if __name__ == '__main__':
    main()