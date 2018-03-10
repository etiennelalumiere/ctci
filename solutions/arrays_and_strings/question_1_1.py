def has_unique_characters(string):
    string = sorted(string)

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True


def main():
    print(has_unique_characters("aosidufy"))
    print(has_unique_characters("aosiadufy"))


if __name__ == '__main__':
    main()