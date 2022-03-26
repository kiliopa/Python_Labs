#! /usr/bin/env python3
# Title : Counting Stack
# Author : Gaylord Kiliopa
# Date : December 2021

#Description : Count all the elements that are pushed and popped (we assume that
# counting pops is enough) in a Stack class.

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter += 1
        return Stack.pop (self)


stk = CountingStack()
for i in range (100):
    stk.push(i)
    stk.pop()
print(stk.get_counter ())
