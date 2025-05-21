class Stack:
    def __init__(self):
        self.__l = []
    
    def push(self, data):
        self.__l.append(data)
    
    def pop(self):
        return self.__l.pop()
    
    def peek(self):
        return self.__l[len(self.__l) - 1]
