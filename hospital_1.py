class Queue:
    def __init__(self) -> None:
        self.__l = []
    
    def enqueue(self, data: any) -> None:
        self.__l.append(data)
    
    def dequeue(self) -> any:
        return self.__l.pop(0)
    
    def peek(self) -> any:
        return self.__l[0]

class Patient:
    def __init__(self, name: str, appointment_time: str):
        self.name = name
        self.appointment_time = appointment_time
