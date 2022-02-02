# one way
# deterministic
# collision can occur if hashing produce same hash value
# calculating hash method -> O(1)
# set_item() -> O(1)
# get_item() -> O(n)

class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def delete_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    self.data_map[index].pop(i)

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(str(i) + " -> " + str(val))


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 100)
my_hash_table.set_item('washers', 20)
my_hash_table.set_item('lumber', 30)
my_hash_table.set_item('nails', 55)
my_hash_table.set_item('screws', 34)
my_hash_table.print_table()

print(my_hash_table.get_item('shaw'))
print(my_hash_table.get_item('nails'))
print(my_hash_table.get_item('bolts'))

print(my_hash_table.keys())

my_hash_table.delete_item('nails')

print('printing after delete...')
my_hash_table.print_table()