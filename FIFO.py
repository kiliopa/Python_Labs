#! /usr/bin/env python3
# Title : Queue aka FIFO
# Author : Gaylord Kiliopa
# Date : December 2021

#Description : A queue is a data model characterized by the term FIFO (first in - First Out)
# Our tsk is to implement the Queue class with two basic operations.  Put (element) which put
# an element at end of the queue; and get () which takes an element from the front
# of the queue qnd returns it qs q result (the queue cqnnot be empty to succefully perform it)

class QueueError (IndexError):
    pass

class Queue:
    def __init__(self):
        self.queue = []

    def put (self, elem):
        self.queue.insert (0,elem)

    def get (self):
        if len(self.queue) > 0 :
            elem = self.queue [-1]
            del self.queue [-1]
            return elem
        else:
            raise QueueError
        

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
