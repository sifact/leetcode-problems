class MyHashMaps:

    def __int__(self, hash_map):
        self.hash_map = {}

    def put(self, key, value):
        self.hash_map[key] = value

    def get(self, key):
        return self.hash_map[key]

    def remove(self, key):
        del self.hash_map[key]


maps = MyHashMaps()
maps.put(2, 2)
maps.put(2, 1)
print(maps.hash_map)
print(maps.get(2))
maps.remove(0)
print(maps.hash_map)
