import node
import random, math

def itinerate(end:int, start:int, nodes:list):
    next = nodes[start].recibe(end)
    if end == start:
        return 0
    d = 1
    while not next == end:
        #print(next)
        next = nodes[next].recibe(end)
        d += 1
    return d

def main():
    nodes = []
    n = 20
    for i in range(n):
        before = n-1 if i == 0 else i-1
        after = 0 if i == n-1 else i+1
        data = [before, after]
        for j in range(int(math.log2(n))):
            data.append(random.randint(0, n-1))
            print(len(data))
        nodes.append(node.node(i, data))
        
    
    
    
    results = []
    for i in range(n):
        for j in range(n):
            results.append(itinerate(j, i, nodes))
       
       
    for result in results:
        print(result, max(results))

        
if __name__ == '__main__':
    main()