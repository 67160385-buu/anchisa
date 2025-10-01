class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data == []:
            return "Stack is empty!"
        else:
            remove = self.data.pop()
            return remove

    def peek(self):
        return self.data[len(self.data) - 1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


s = Stack()

for i in range(1, 6):
    s.push(i)

print("Is empty?", s.is_empty())

print("Size after push:", s.size())
print("Top element:", s.peek())

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())