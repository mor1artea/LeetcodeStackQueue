class MyStack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0

    def _enqueue(self, x):
        node = [x, None]
        if self.tail is not None:
            self.tail[1] = node
        else:
            self.head = node
        self.tail = node
        self.sz += 1

    def _dequeue(self):
        val = self.head[0]
        self.head = self.head[1]
        if self.head is None:
            self.tail = None
        self.sz -= 1
        return val

    def push(self, x):
        n = self.sz
        self._enqueue(x)
        for _ in range(n):
            self._enqueue(self._dequeue())

    def pop(self):
        return self._dequeue()

    def top(self):
        return self.head[0]

    def empty(self):
        return self.head is None
