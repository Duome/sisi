# -*- coding: utf-8 -*-
class Sstack(object):
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not self.stack

    def pop(self):
        assert self.is_empty()
        info = self.stack.pop()
        return info

    def push(self, item):
        self.stack.append(item)

# 从尾进，从尾出
class Lstack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return not self.size

    def prepare(self, item):
        # 后一个指针的next属性即为上一个指针
        self.top = Node(item, self.top)
        self.size += 1

    def pop(self):
        assert not self.is_empty()
        info = self.top.item
        self.top = self.top.next
        return info


class Node(object):
    def __init__(self, item, next_=None):
        self.item = item
        self.next_ = next_
