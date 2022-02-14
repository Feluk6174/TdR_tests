from pickletools import read_string1


class node():
    def __init__(self, id, data):
        self.id = id
        self.data = data
        #print(self.id, self.data)
        
    def recibe(self, data):
        for i, n in enumerate(self.data):
            if i == 0:
                smallest = [abs(data-n), n]
            elif smallest[0] > abs(data-n):
                smallest = [abs(data-n), n]
        return smallest[1]
            