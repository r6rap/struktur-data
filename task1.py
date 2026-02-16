class StaticArray:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("size harus positif")
        self._size = size
        self._data = [0] * size

    def size(self):
        return self._size

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index di luar ukuran array")
        return self._data[index]

    def set(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("index di luar ukuran array")
        self._data[index] = value
    def __repr__(self):
        return f"StaticArray({self._data})"



class DynamicArray:
    def __init__(self, capacity=1):
        if capacity <= 0:
            raise ValueError("kapasitas harus positif")
        self._capacity = capacity
        self._size = 0
        self._data = [0] * capacity

    def size(self):
        return self._size

    def push_back(self, value):
        if self._size == self._capacity:
            self._resize()

        self._data[self._size] = value
        self._size += 1

    def _resize(self):
        new_capacity = self._capacity * 2
        new_data = [0] * new_capacity

        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data
        self._capacity = new_capacity

    def __repr__(self):
        return f"DynamicArray(size={self._size}, data={self._data[:self._size]})"


# static
print("\nstatic Array:")
s = StaticArray(3)
print("ukuran static array:", s.size())
s.set(0, 10)
print("nilai index 0:", s.get(0))
s.set(1, 20)
print("nilai index 1:", s.get(1))
print(s)
print("index 2 0 karena belum diisi")

# dynamic
print("\ndynamic Array:")
d = DynamicArray(2)
print("ukuran dynamic array:", d.size())
d.push_back(5)
print("masukkan 5 ke index 0")
d.push_back(15)
print("masukkan 15 ke index 1")
d.push_back(25)
print("masukkan 25 ke index 2, kapasitas bertambah otomatis")
print(d)