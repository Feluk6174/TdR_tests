class node():
    def __init__(self, id:int, known_nodes:list):
        self.id = id
        self.known_nodes = known_nodes

    def resend(self, destination:int):
        for i, node_id in enumerate(self.known_nodes):
            if i == 0:
                smallest = abs(destination-node_id), 