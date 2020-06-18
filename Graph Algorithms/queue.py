class Queue:

    def __init__(self):
        self.values = []
    
    def IsEmpty(self):
        if (len(self.values) < 1):
            return True
        return False
    
    def Enqueue(self, val):
        self.values.append(val)
    
    def Dequeue(self):
        dequeuedVal = self.values.pop(0)
        return dequeuedVal
    
    def GetQueue(self):
        return self.values
