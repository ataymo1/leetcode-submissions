class MyHashMap:

    def __init__(self):
        self.table = [[] for i in range(100)]

    def put(self, key: int, value: int) -> None:
        actual_key = key % len(self.table)
        small_table = self.table[actual_key]
        for i, items in enumerate(small_table):
            rkey, chud = items
            if rkey == key:
                small_table[i] = tuple((key, value))
        self.table[actual_key].append(tuple((key, value)))

    def get(self, key: int) -> int:
        actual_key = key % len(self.table)
        small_table = self.table[actual_key]

        for rkey, value in small_table:
            if rkey == key:
                return value
        return -1
    def remove(self, key: int) -> None:
        actual_key = key % len(self.table)
        small_table = self.table[actual_key]
        for i, items in enumerate(small_table):
            rkey, value = items
            if rkey == key:
                small_table[i] = tuple((-1, -1))
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)