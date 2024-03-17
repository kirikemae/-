class LimitedStack:
    def __init__(self, limit):
        self.limit = limit
        self.stack = [None] * self.limit
        self.size = 0

    def push(self, item):
        if self.limit != 0:
            if self.size == self.limit:
                self.size = 0
            self.stack[self.size] = item
            self.size += 1
        return "ok"

    def pop(self):
        self.size -= 1
        if self.size < 0:
            self.size = self.limit - 1
        value = self.stack[self.size]
        return value

    def count(self):
        return self.limit - self.stack.count(None)


if __name__ == "__main__":
    limit = int(input())

    stack = LimitedStack(limit)
    out = ""
    while True:
        command = input().split()
        operation = command[0]
        if operation == "push":
            value = int(command[1])
            out += stack.push(value) + "\n"
        elif operation == "pop":
            out += f"{stack.pop()}\n"
        elif operation == "count":
            out += f"{stack.count()}\n"
        elif operation == "exit":
            out += "bye"
            break
    print(out)
