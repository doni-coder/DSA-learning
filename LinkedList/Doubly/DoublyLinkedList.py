class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.prev = prev
        self.data = data
        self.next = next


class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        if self.start == None:
            return self.start == None

    def search(self, data):
        temp = self.start
        if self.start == None:
            return None
        else:
            while temp is not None:
                if temp.data == data:
                    return temp
                else:
                    temp = temp.next
            return temp

    def insert_at_first(self, data):
        new_node = Node(data=data)
        if self.start == None:
            new_node.next = self.start
        else:
            new_node.next = self.start
            self.start.prev = new_node
        self.start = new_node

    def insert_after(self, position, data):
        node = self.search(data=position)
        new_node = Node(data=data)
        if node == None:
            print("can't found data")
        elif node.next == None:
            node.next = new_node
            new_node.prev = node
            new_node.next = None
        else:
            new_node.prev = node
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node

    def insert_at_last(self, data):
        new_node = Node(data=data)
        temp = self.start
        if self.start.next == None:
            new_node.prev = self.start
            self.start.next = new_node
        else:
            while temp is not None:
                temp = temp.next
            new_node.prev = temp
            temp.next = new_node

    def delete_at_first(self):
        if self.start is None:
            return None
        elif self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next

    def delete_n(self, data):
        node = self.search(data)
        if node is None:
            return
        if node.prev != None:  # instead of "is not None"
            node.prev.next = node.next
        else:
            self.start = node.next
        if node.next != None:  # instead of "is not None"
            node.next.prev = node.prev

    def delete_at_last(self):
        temp = self.start
        if temp == None:
            return None
        elif temp.next == None:
            self.start = None
        else:
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


my_list = DLL()
my_list.insert_at_first(5)
my_list.insert_at_first(30)
my_list.insert_at_first(20)
my_list.insert_at_first(10)

# my_list.insert_after(40, 100)
my_list.print_list()
# my_list.delete_n(10)  
my_list.delete_n(20)
my_list.delete_n(30)
my_list.delete_n(5)
# my_list.delete_at_first()
# my_list.delete_at_last()
print("\n")
my_list.print_list()
