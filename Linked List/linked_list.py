class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def countNode(head):
    length = 1
    current = head
    while True:
        if current.next is not None:
            length += 1
            current = current.next
        else:
            break
    return length


head = Node(4)
nodeB = Node(2)
head.next = nodeB
nodeC = Node(3)
nodeB.next = nodeC
nodeD = Node(10)
nodeC.next = nodeD

length = countNode(head)
print(length)
