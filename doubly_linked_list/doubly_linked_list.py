"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        current = self.head
        l_len = 0
        while current:
            l_len +=1
            current = current.next
        return l_len

    def add_to_head(self, value):
        if not self.head and not self.tail:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

    def add_to_tail(self, value):
        if not self.head and not self.tail:
            self.head = ListNode(value)
            self.tail = self.head
        else: 
            self.tail.insert_after(value)
            self.tail = self.tail.next
            #print(f'new tail: {self.tail.value}, new prev {self.tail.prev.value}')


    def remove_from_head(self):
        if not self.head:
            self.head = None
        if not self.tail:
            self.tail = None
        else:
            self.head.delete()
            self.head = self.head.next
            
    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None
        else:
            self.tail.delete()
            self.tail = self.tail.prev
            
    def move_to_front(self, node):
        if not node.prev:
            return
        else:
            node.delete()
            self.add_to_head(node.value)
            node.prev = self.head.prev
            node.next = self.head.next
            
            
    def move_to_end(self, node):
        curr_prev = node.prev
        curr_next = node.next
        
        if curr_next != None:
            if curr_prev != None:
                curr_next.prev = curr_prev
                curr_prev.next = curr_next
            else:
                curr_next.prev = None
                self.head = curr_next
                
        prev_tail = self.tail
        self.tail = node
        node.prev = prev_tail
        node.next = None
        prev_tail.next = node
        
    def delete(self, node):
        if node:
            if node == self.head and node == self.tail:
                self.head = None
                self.tail = None
                
            elif node.prev == None:
                self.remove_from_head()
                
            elif node.next == None:
                self.remove_from_tail()
                
        node.delete()
        
    def get_max(self):
        current = self.head
        vals = []
        while current:
            vals.append(current.value)
            current = current.next
        return max(vals)
    