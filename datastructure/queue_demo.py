# -*- coding: utf-8 -*-
#从头进，从尾出，列表的头是队列的尾，列表的尾是队列的头
class SQueue(object):

    def __init__(self):
        self._item = []

    def is_empty(self):
        return not self._item

    def dnqueue(self):
        assert not self.is_empty()
        return self._item.pop(0)

    def enqueue(self, item):
        self._item.append(item)
#出队操作是rear什么意思？这里的rear是指指针
class LQueue(object):
    def __init__(self):
        self._front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return not self.size

    def dnqueue(self):
        assert not self.is_empty()
        info = self._front
        self._front = info.next
        return info.item

    def enqueue(self, item):
        pin = Node(item)
        if self.is_empty():
            self._front = self.rear = pin
        else:
            # 为什么这里使用self.rear.next会报AttributeError: can't set attribute
            self.rear._next = pin
            self.rear = pin
        self.size += 1


class Node(object):
    def __init__(self, item):
        self._item = item
        self._next = None

    @property
    def item(self):
        return self._item

    @property
    def next(self):
        return self._next

if __name__ == '__main__':
    q = LQueue()
    print(q.is_empty())
    q.enqueue(1)
    print(q._front.next)
    print(q.is_empty())
    q.enqueue(2)
    print(q.is_empty())
    print(q.dnqueue())
    print(q.dnqueue())
    print(q.is_empty())
