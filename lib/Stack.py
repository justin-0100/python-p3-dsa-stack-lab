class Stack:
    def __init__(self, items=None, limit=100):
        self._stack = items if items is not None else []
        self._limit = limit

    @property
    def items(self):
        return self._stack

    def isEmpty(self):
        return len(self._stack) == 0

    def push(self, item):
        if not self.full():
            self._stack.append(item)
        # If full, do nothing (test doesn't want an error)

    def pop(self):
        if self.isEmpty():
            return None
        return self._stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self._stack[-1]

    def size(self):
        return len(self._stack)

    def full(self):
        return len(self._stack) >= self._limit

    def search(self, target):
        for index_from_top, value in enumerate(reversed(self._stack)):
            if value == target:
                return index_from_top
        return -1
