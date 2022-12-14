# Linked list class and support classes.
#

#1.2) Singly linked lists outperform list() for insertion because it does not need to index, it just needs to find the head of the value it is prepending. 
#It also takes longer for singly linked lists to use the length function for this same reason, as it has to go through every node manually to count the length




class ListNode(object):
    '''Represents an item on a linked list.

    There are two attributes, one to hold the value stored in
    the list, the next "points" to the next node on the list.
    The last node on the list always has its link set to some
    "sentinel" value, such as None in Python or null in Java.
    '''
    def __init__(self, val, lnk = None):
        '''Construct a list node.'''
        self.value = val
        self.link = lnk

class SinglyLinkedList(object):
    '''Class that defines a relatively simple linked list, with a
    single link leading from a predecessor node to a successor node.

    Implements several methods, modeled on those in the standard
    list() class. In addition, implements a "prepend()" method that
    illustrates adding an element to the beginning of a list.

    Methods of the standard list class that we do not implement include:
    clear(), copy(), extend(), __add__(), __mul__(), reverse(), and sort().
    '''
    def __init__(self, iterable = ()):
        '''Creates a new list, initialized to the contents of 
        'iterable'.'''
        self.head = None # start with an empty linked list.
        previous = None  # append elements from iterable to the new list.
        for value in iterable:
            newnode = ListNode(value)
            if previous == None:
                self.head = newnode
            else:
                previous.link = newnode
            previous = newnode
    
    def clear(self):
        '''
        Clears the list
        '''
        node = self.head
        while node != None:
            node = node.link # go to the next node

    def copy(self):
        b = SinglyLinkedList()
        node = self.head
        while node.link != None:
            b.append(node.value)
            node = node.link
        b.append(node.value)
        return b

    def remove(self, value):
        previous = None
        node = self.head
        while node != None and node.link != None:
            if node.value == value:
                self.head == self.head.link
                return node
            else:
                previous = node
                node = node.link
        previous = node
        node = node.link
        return previous
        
    def __gt__(self, other):
        list1 = self.head
        list2 = other.head
        while True:
            if list1 > list2:
                return True
            else:
                if list1 == None or list2 == None:
                    return False
                else:
                    list1  = list1 .link
                    list2 = list2.link

    def __add__(self,other):
        newList = SinglyLinkedList()
        list1 = self.head
        list2 = other.head
        while list1 != None:
            newList.append(list1)
            list1  = list1 .link
        while list2 != None:
            newList.append(list2)
            list2 = list2.link
        return newList

    def reverse(self):
        newList = SinglyLinkedList()
        node = self.head
        while node != None:
            newList.prepend(node)
            node = node.link


    def pop(self, index = -1):
        '''Removes an node from the list based on a given
        index. If the index is -1, the last node on list is
        removed. Returns the value associated with the deleted
        node.'''
        count = 0
        previous = None
        node = self.head
        if index >= 0:
            while node != None and count != index:
                count += 1
                previous = node
                node = node.link
        else:
            while node != None and node.link != None:
                previous = node
                node = node.link
        if node == None:
            raise ValueError('Position ' + str(index) + ' not found.')
        
        if previous != None:
            previous.link = node.link
        else:
            self.head = node.link

        return node.value

    def prepend(self, value):
        '''Add an element to the beginning of the list.

        This is the easiest case. All we need to do is:
        1) create the new list node
        2) set the link field of the new node to the
        current list head.
        3) set the current list head to this node.
        '''
        node = ListNode(value)
        node.link = self.head
        self.head = node
        
    def get(self, index):
        '''Get the value stored at a particular index
        of the linked list.

        To accomplish this, we have to look through every node
        on the list, counting up as we go. When the count reaches
        the index, we return the value found there.'''
        count = 0
        node = self.head
        while node != None:
            if count == index:
                return node.value
            node = node.link
            count += 1
        raise IndexError('list index out of range')

    def count(self, value):
        '''Count the number of list nodes with values equal to the
        'value'.'''
        count = 0
        node = self.head
        while node != None:
            if node.value == value:
                count += 1
            node = node.link
        return count

    def index(self, value):
        '''Return the index of the first list element that matches
        the given 'value'.'''
        count = 0
        node = self.head
        while node != None:
            if node.value == value:
                return count
            count += 1
            node = node.link
        raise ValueError('Value ' + str(value) + ' not found.')
            
    def append(self, value):
        '''Add an element to the end of the linked list.

        This method has to be a bit more complex than the
        prepend() method, in that we have to search to the
        end of the list, and insert the new node there.
        '''
        node = self.head
        if node == None:    # Empty list
            self.head = ListNode(value)
        else:
            while node.link != None:
                node = node.link
            node.link = ListNode(value)

    def insert(self, index, value):
        '''Add an element at a particular index of a linked
        list.
        If the index is greater than the length of the list, the
        new node is just appended to the list.'''
        newnode = ListNode(value)
        node = self.head
        if index == 0:
            newnode.link = self.head
            self.head = newnode
        else:
            count = 1
            while node.link != None and count < index:
                node = node.link
                count += 1
            newnode.link = node.link
            node.link = newnode
        
    

    def __bool__(self):
        '''Returns True if the list is non-empty.

        This method is called implicitly when a value of our class
        is converted to a Boolean value.'''
        return self.head != None

    def __len__(self):
        '''Returns the total number of nodes on the list.

        This method is called implicitly when the len() function
        is used with values of this class.'''
        count = 0
        node = self.head
        while node != None:
            count += 1       # count the node
            node = node.link # go to the next node
        return count

    def __str__(self):
        '''Convert a linked list to a string representation.

        This method is called implicitly when the str() function
        is used with values of this class.
        '''
        node = self.head
        r = '['
        while node != None:
            r += repr(node.value)
            if node.link != None: # If not at the end,
                r += ', '         #  add a comma and space.
            node = node.link
        r += ']'
        return r

    def __eq__(self, other):
        '''Compare two linked lists for equality.

        This method is called when a SinglyLinkedList is
        compared with '==' or '!='. It assumes that 'other'
        is also a SinglyLinkedList.
        '''
        if other is None:
            return False
        node1 = self.head
        node2 = other.head
        while node1 != None and node2 != None:
            if node1.value != node2.value:
                return False
            node1 = node1.link
            node2 = node2.link
        return node1 == None and node2 == None

    def __iter__(self):
        '''Implement Python iteration.'''
        return ListIter(self.head)

class ListIter(object):
    '''Class that represents a list iterator.

    An iterator object normally implements the __next__() method, which
    either returns the next value on the iterator, or raises StopIteration.
    '''
    def __init__(self, head):
        '''Initialize the iterator.'''
        self.cursor = head
    def __next__(self):
        '''Advance to the next item in the iterator.'''
        if self.cursor != None:
            result = self.cursor
            self.cursor = result.link
            return result.value
        raise StopIteration()

### Testing code ###
#
# As of now, the testing code is quite haphazard, but it attempts to
# exercise all of the features of the class. In addition, it runs a
# simple timing check to illustrate some of the performance
# differences between this class and the Python list() class.
#
if __name__ == "__main__":
    print("Testing the SinglyLinkedList class.")
    r = SinglyLinkedList()
    r.prepend(5)
    r.prepend(100)
    assert str(r) == "[100, 5]"
    assert r.get(0) == 100
    assert r.get(1) == 5
    
    s = SinglyLinkedList(range(1, 11))
    assert all(s.index(x) == x - 1 for x in s)

    #NEW Tests
    a = r.copy()
    assert a == r
    assert a is not r

    a = SinglyLinkedList([1, 1, 2])
    b = SinglyLinkedList([1, 1, 2])
    assert not (a > b)
    a.append(1)
    assert a > b
    a = SinglyLinkedList([1, 1, 3])
    assert a > b


    r = SinglyLinkedList([5, 1, 9, 8, 5, 2])
    assert r.get(0) == 5
    assert r.get(5) == 2
    r.remove(2)
    r.remove(5)
    r.remove(5)
    assert len(r) == 3
    assert r.get(0) == 1
    try:
        r.remove(5)
    except ValueError:
        pass # caught the exception
    else:
        assert False # Error, no exception.


    for i in range(10, 0, -1):
        assert s.index(i) == i - 1
        assert s.get(i - 1) == i
    s.pop(8)
    assert len(s) == 9
    assert s.count(9) == 0
    s.pop(1)                    # remove second value.
    assert len(s) == 8
    assert s.get(1) == 3
    s.pop()                     # remove final value.
    assert len(s) == 7
    assert s.get(6) == 8
    assert s.pop(0) == 1
    assert s.get(0) == 3
    s.pop(0)
    assert len(s) == 5
    assert s.get(0) == 4
    s.pop(4)
    assert len(s) == 4
    assert s.get(0) == 4

    t = SinglyLinkedList()
    assert str(t) == "[]"
    assert len(t) == 0
    try:
        t.pop()
    except ValueError as ex:
        pass
    else:
        assert False
    try:
        t.index(10)
    except ValueError as ex:
        pass
    else:
        assert False
    t.append(10)
    t.append(21)
    t.append(19)
    assert t.index(10) == 0
    assert t.index(21) == 1
    assert str(t) == "[10, 21, 19]"
    t.insert(100, 55)
    t.insert(1, 1)
    t.insert(5, 8)
    t.insert(1, 21)
    assert t.count(21) == 2
    assert t.count(22) == 0
    try:
        y = t.index(22)
    except ValueError as ex:
        pass
    else:
        assert False

    while t:
        t.pop()

    x1 = SinglyLinkedList([5, 10])
    x2 = SinglyLinkedList([5, 10])
    assert x1 == x2
    x2.append(8)
    assert x1 != x2
    x1.append(8)
    assert x1 == x2
    x1.append(5)
    assert x1 != x2
    x1.pop()
    assert x1 == x2

    # Make sure the iterator works.
    assert [v for v in x1] == [5, 10, 8]

    # See if content testing works
    a = SinglyLinkedList([5, 1, 9, 8])
    assert 1 in a
    assert 8 in a
    assert 6 not in a

    print("All tests passed.")
    
    # Performance check. Compare the time taken for
    # many calls to insert() and len() (remember that
    # calling len() on a SinglyLinkedList() will call
    # the __len__() method defined above.
    #
    def performance(x):
        '''Function to compute and display timing information
        for the insert() and len() functions of an iterable list.'''
        import time
        start = time.time()
        for i in range(100000):
            x.insert(0, i)
        elapsed = time.time() - start
        print('insert(): {:.5f} sec.'.format(elapsed))
        start = time.time()
        for i in range(1000):
            t = len(x)
        elapsed = time.time() - start
        print('len() {:.5f} sec.'.format(elapsed))

    print("Performance of Python list()")
    performance(list())
    print("Performance of SinglyLinkedList()")
    performance(SinglyLinkedList())
