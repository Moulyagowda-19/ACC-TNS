class HashTable:
    def __init__(s):
        s.bucket = [
            [] for _ in range (7)]
    def _hash(s,key):
        return sum(ord (c)
            for c in key) % 7
    def insert(s,k,v):
        i = s._hash(k)
        s.bucket[i].append(
            (k,v))
    def search(s,key):
        i = s._hash(key)
        for k,v, in s.bucket[i]:
            if k == key:
                return v
        return None