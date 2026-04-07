from collections import defaultdict, deque

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(deque)
        self.max_freq = 0

    def push(self, val):
        self.freq[val] += 1
        f = self.freq[val]
        self.group[f].append(val)
        if f > self.max_freq:
            self.max_freq = f

    def pop(self):
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
