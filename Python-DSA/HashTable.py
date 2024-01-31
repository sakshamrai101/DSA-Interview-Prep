class HashTable:
    def __init__(self, size = 7):
        # Empty list initialised with the passed in size.
        self.data_map = [None] * size

    def _hash(self, key):
        my_hash = 0
        for letter in key:
            # Ord function gives the ASCII value of the letter. 
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

            # my_hash will have value from 0 to 6, equal to our sample space. 
            # that is why modded by length of the list which is a prime number. 
        return my_hash
    
    def print_table(self):
        for key, value in enumerate(self.data_map):
            print(key, ": ", value)

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self._hash(key)

        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None 
    
    def keys(self):
        key_list = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    key_list.append(self.data_map[i][j][0])
        return key_list
    


def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False
    
                



my_table = HashTable(7)
my_table.set_item('bolts', 1000)
my_table.set_item('washers', 50)
my_table.set_item('lumber', 20)
my_table.set_item('nuts', 2000)
my_table.print_table()


list1 = [1, 2, 3]
list2 = [6, 7, 9]
print(item_in_common(list1, list2))

print(my_table.keys())


