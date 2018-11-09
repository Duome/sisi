# -*- coding: utf-8 -*-
class SStack(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not self._items

    def pop(self):
        assert self.is_empty()
        info = self._items.pop()
        return info

    def push(self, item):
        self._items.append(item)

# 从栈尾进，从栈尾出，栈头头列表的尾
class LStack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return not self.size

    def push(self, item):
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
        self._item = item
        self._next = next_

    @property
    def item(self):
        return self._item

    @property
    def next(self):
        return self._next
