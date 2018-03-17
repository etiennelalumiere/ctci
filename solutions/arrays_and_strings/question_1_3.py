from collections import deque

def urlify(s, n):
    s = list(s)
    j = len(s) - 1

    for i in range(n - 1, -1, -1):
        if s[i] == ' ':
            s[j - 2:j + 1] = '%20'
            j -= 3
        else:
            s[j] = s[i]
            j -= 1

    return ''.join(s)


def main():
    print(urlify('Mr A John Qwerty      ', 16))


if __name__ == '__main__':
    main()