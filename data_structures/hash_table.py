class HashTable:
    def __init__(self):
        self.size = 5
        self.table = [[] for i in range(self.size)]
        print(self.table)

    def get(self, key):
        index = self.__hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def put(self, key, value):
        index = self.__hash_function(key)
        self.table[index].append((key, value))
        print(self.table)

    def __hash_function(self, value):
        return abs(hash(value) % self.size)


def main():
    hash_table = HashTable()

    print(hash_table.get(45))
    print(hash_table.get("chat"))

    hash_table.put("chat", 23)
    hash_table.put("chien", 10)
    hash_table.put("tortue", 21)
    hash_table.put("perruche", 54)
    hash_table.put("poisson", 1000)

    print(hash_table.get("chat"))
    print(hash_table.get("chien"))
    print(hash_table.get("tortue"))
    print(hash_table.get("perruche"))
    print(hash_table.get("poisson"))


if __name__ == '__main__':
    main()