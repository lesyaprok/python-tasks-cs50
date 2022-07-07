class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = 0
    def __str__(self):
        return "🍪" * self.size
    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n
    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self.size -= n
    @property
    def _capacity(self):
        return self.capacity

    @property
    def _size(self):
        return self.size


def main():
    cap = int(input("Capacity: "))
    jar = Jar(cap)
    print(jar.capacity)


if __name__ == "main":
    main()
