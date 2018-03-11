from random import randint


def train_dec_to_bits():
    while 1:
        correct_number = randint(0, 64)
        user_number = input('decimal = %d\n' % correct_number)

        if int(user_number, 2) == correct_number:
            print('good!')
        else:
            print('wrong! {0:b}'.format(correct_number))


def train_and_operator():
    while 1:
        a = randint(0, 64)
        b = randint(0, 64)
        a_and_b = a & b
        print('{:8b}'.format(a))
        print('{:8b}'.format(b))
        user_a_and_b = input()

        if int(user_a_and_b, 2) == a_and_b:
            print('good!')
        else:
            print('wrong! {:8b}'.format(a_and_b))


def train_or_operator():
    while 1:
        a = randint(0, 64)
        b = randint(0, 64)
        a_or_b = a | b
        print('{:8b}'.format(a))
        print('{:8b}'.format(b))
        user_a_or_b = input()

        if int(user_a_or_b, 2) == a_or_b:
            print('good!')
        else:
            print('wrong! {:8b}'.format(a_or_b))


if __name__ == '__main__':
    train_or_operator()
