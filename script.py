####  This is a Last In, First Out or LIFO structure. A less frequently used term is First In, Last Out, or FILO.
from node import Node

# Add your Stack class below:
class Stack1:
  def __init__(self):
    self.top_item = Node(None)
    
  def peek(self):
    return self.top_item.get_value()

sta = Stack1()
print(sta.peek())

from node import Node

class Stack:
  def __init__(self):
    self.top_item = Node(None)
  
  # Define your push() and pop() methods below:
  def push(self, value):
    self.top_item = Node(value, self.top_item)
  def pop(self):
    item_to_remove = self.top_item
    self.top_item = item_to_remove.get_next_node()
    return item_to_remove.get_value()
  
  def peek(self):
    return self.top_item.get_value()

from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.limit = limit
    self.size = 0
  
  def push(self, value):
    item = Node(value)
    item.set_next_node(self.top_item)
    self.top_item = item

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      # Decrement the stack size here:
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is empty.")
  
  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    else:
      print("Nothing here!")

from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit

  def has_space(self):
    if self.size < self.limit:
      return True
    else:
      Print("No space left in the stack")
  def is_empty(self):
    if self.size > 0:
      return False
    else:
      return True
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      # Increment stack size by 1 here:
      self.size += 1

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
  
  def peek(self):
    if self.size > 0:
	    return self.top_item.get_value()
    else:
      print("Nothing to see here!")
      
from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the pizza stack!".format(value))
    else:
      print("No room for {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()


  
