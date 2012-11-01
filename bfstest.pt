class Myqueue:
    def __init__(self):
        self.holder = []


    def enqueue(self,var):
        self.holder.append(var)

    def dequeue(self):
        val = None
        try:
            val = self.holder[0]#the first element
            if len(self.holder) == 1:
                self.holder =[]
            else:
                self.holder = self.holder[1:]
        except:
            pass
        return val
