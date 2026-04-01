class MyHashSet:

    def __init__(self):
        self.table = [list()] * 100
        

    def add(self, key: int) -> None:
        actual_key = key % len(self.table)
        small_table = self.table[actual_key]
        for n in small_table:
            if n == key:
                return
        self.table[actual_key].append(key)

    def remove(self, key: int) -> None:
        actual_key = key % len(self.table)
        small_table = self.table[actual_key]
        for n in small_table:
            if n == key:
                small_table.remove(key)

    def contains(self, key: int) -> bool:
        actual_key = key % len(self.table)
        small_table = self.table[actual_key]
        for n in small_table:
            if n == key:
                return True
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)