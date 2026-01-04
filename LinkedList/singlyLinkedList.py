class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(item=data, next=self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(item=data, next=None)
        if not self.is_empty():
            # traverse the list
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert(self, temp, data):
        if temp is not None:
            n = Node(item=data, next=temp.next)
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

    def delete_from_first(self):
        temp = self.start
        if temp is not None:
            self.start = temp.next

    def delete_from_last(self):
        temp = self.start
        if temp.next == None:
            return None
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def insert_after(self, node, data):
        n = Node(item=data)
        print(node)
        n.next = node.next
        node.next = n

    def __iter__(self):
        return SLLIterator(self.start)
    
    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     if not self.start:
    #         raise StopIteration
    #     data = self.start
    #     self.start = self.start.next
    #     return data.item
    


class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current
        self.current = self.current.next
        return data.item


my_list = SLL()
my_list.insert_at_start(20)
my_list.insert_at_start(30)
my_list.insert_at_start(40)
my_list.insert_after(my_list.search(30), 100)
# my_list.insert_at_last(100)
# my_list.insert_at_start(400)
# my_list.delete_from_last()
# my_list.delete_from_last()

my_list.print_list()
print("\n-------------------")
for item in my_list:
    print(item)
# my_list.delete_item(10)
# my_list.print_list()
