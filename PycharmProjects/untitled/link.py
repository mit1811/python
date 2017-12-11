class Node(object):
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next_node=next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self,new_next):
        self.next_node=new_next

class LinkedList(object):
    def __init__(self,head=None):
        self.head=head
    def size(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.get_next()
        return count
    def search(self):
        current=self.head
        found=False
        while current and found is False:
            if current.get_data()==data:
                found = True
            else:
                current=current.get_next()
        if current is None:
            raise ValueError("data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
mylist=LinkedList()
mylist.add(5)
mylist.add(10)
mylist.add(15)
print mylist
