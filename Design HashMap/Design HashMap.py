class MyHashMap:

    def __init__(self):
        self.arr = list()

    def put(self, key: int, value: int) -> None:
        if len(self.arr) <= key:
            newArr = [self.arr[i] if i < len(self.arr) else None for i in range(key+1)]
            self.arr = newArr
        
        self.arr[key] = value

    def get(self, key: int) -> int:
        if key >= len(self.arr):
            return -1
        
        if self.arr[key]:
            return self.arr[key]

        return -1

    def remove(self, key: int) -> None:
        if key >= len(self.arr):
            return 
            
        self.arr[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)