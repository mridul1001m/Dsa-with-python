class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

  
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

   
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

  
    def delete(self, key):
        if not self.head:
            return

        curr = self.head
        prev = None

        while True:
            if curr.data == key:
                if prev:
                    prev.next = curr.next
                else:
               
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = self.head.next
                    self.head = self.head.next
                return
            prev = curr
            curr = curr.next
            if curr == self.head:
                break

    
    def display(self):
        nodes = []
        if not self.head:
            return nodes
        temp = self.head
        while True:
            nodes.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        return nodes


cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.prepend(5)
print("Circular Linked List:", cll.display())
cll.delete(20)
print("After deleting 20:", cll.display())