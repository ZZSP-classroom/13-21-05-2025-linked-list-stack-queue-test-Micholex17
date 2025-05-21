class Queue:
    def __init__(self) -> None:
        self.__l = []
    
    def enqueue(self, data: any) -> None:
        self.__l.append(data)
    
    def dequeue(self) -> any:
        return self.__l.pop(0)
    
    def peek(self) -> any:
        if len(self.__l) > 0:
            return self.__l[0]
        else:
            return None

class Stack:
    def __init__(self):
        self.__l = []
    
    def push(self, data):
        self.__l.append(data)
    
    def pop(self):
        return self.__l.pop()
    
    def peek(self):
        return self.__l[len(self.__l) - 1]

class Call:
    def __init__(self, caller_id, time_received):
        self.caller_id = caller_id
        self.time_received = time_received

class CallCenter:
    def __init__(self):
        self.incoming_calls = Queue()
        self.processed_calls = Stack()
    
    def add_call(self, new_call):
        self.incoming_calls.enqueue(new_call)
    
    def process_call(self):
        if self.incoming_calls.peek() is not None:
            self.processed_calls.push(self.incoming_calls.dequeue())
    
    def end_call(self):
        self.processed_calls.pop()
