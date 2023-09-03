# Based on this video: https://www.youtube.com/watch?v=vBxmYemGUWk

class HashTable:
    def __init__(self) -> None:
        self.size = 4
        self.hashmap = [[] for i in range(0, self.size)]
    
    def hashing_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key
    
    def set(self, key, value):
        hash_key = self.hashing_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]

        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break

        if key_exists:
            slot[i] = ((key, value))
        else:
            slot.append((key, value))

    def get(self, key):
        hash_key = self.hashing_func(key)
        slot = self.hashmap[hash_key]
        print(f"slot: {slot}")
        for kv in slot:
            k, v = kv
            if key == k:
                return v
        return None
    
    def __setitem__(self, key, value):
        return self.set(key, value)
    
    def __getitem__(self, key):
        return self.get(key)


table = HashTable()

print("\nfilling the hash table using set")
table.set("asdfasdf", "12341234")
table.set("asdfasdfa", "123412341")
table.set("asdfasdfb", "123412342")
table.set("asdfasdfc", "123412343")
table.set("asdfasdfd", "123412344")
table.set("asdfasdfe", "123412345")
table.set("asdfasdff", "123412346")
table.set("asdfasdfg", "123412347")
table.set("sdfgsdfg", "23452345")
table.set("dfghdfgh", "34563456")
table.set("gfhjfghj", "45674567")

print("\nfilling the hash table using brackets []")
table["key1"] = "1234"

print("\nreading from the hash table using get")
print(table.get("dfghdfgh"))
print(table.get("zxcvzxcv"))

print("\nreading from the hash table using brackets []")
print(table["key1"])
