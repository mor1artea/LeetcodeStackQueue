class MyQueue:

    def __init__(self):
        self.in_top = None
        self.out_top = None

    def _push_stk(self, stk_attr, x):
        top = getattr(self, stk_attr)
        setattr(self, stk_attr, (x, top))

    def _pop_stk(self, stk_attr):
        node = getattr(self, stk_attr)
        setattr(self, stk_attr, node[1])
        return node[0]

    def _peek_stk(self, stk_attr):
        return getattr(self, stk_attr)[0]

    def _empty_stk(self, stk_attr):
        return getattr(self, stk_attr) is None

    def _move(self):
        if self._empty_stk("out_top"):
            while not self._empty_stk("in_top"):
                self._push_stk("out_top", self._pop_stk("in_top"))

    def push(self, x):
        self._push_stk("in_top", x)

    def pop(self):
        self._move()
        return self._pop_stk("out_top")

    def peek(self):
        self._move()
        return self._peek_stk("out_top")

    def empty(self):
        return self._empty_stk("in_top") and self._empty_stk("out_top")
