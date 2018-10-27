# -*- coding: utf-8 -*-
#从头出，从尾进
class Squeue(object):

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return not self.queue

    def dnqueue(self):
        assert not self.is_empty()
        return self.queue.pop(0)

    def enqueue(self, item):
        self.queue.append(item)

class Lqueue(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return not self.size

    def pop(self):
        assert not self.is_empty()
        info = self.front.item
        self.front.next = self.front
        return info

    def prepare(self, item):
        pin = Node(item)
        if self.is_empty():
            self.front = self.rear = pin
        else:
            self.rear.next = pin
            self.rear = pin
        self.size += 1


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

if __name__ == '__main__':
    q = Lqueue()
    print(q.is_empty())
    q.prepare(1)
    print(q.is_empty())
    q.prepare(2)
    print(q.is_empty())
    q.pop()
    q.pop()
    print(q.is_empty())