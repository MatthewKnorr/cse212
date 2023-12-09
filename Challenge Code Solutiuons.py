#########################
# 1) Challenge Solution #
#########################
# Python code for the "Message Queue" challenge problem
from queue import Queue

class MessageQueue:
    def __init__(self):
        # Intentional Error: 
        # Incorrect attribute name for the message queue
        self.message_list = Queue() # Fix: Change 'self.message_list' to 'self.queue'

    def send_message(self, message):
        # Intentional Error: 
        # Incorrect method used for sending a message to the queue, Using append() instead of enqueue() to add a message
        self.message_list.append(message)  # Fix: Change 'append' to 'enqueue'
        print(f"Message sent: {message}")

    def receive_messages(self):
        # Intentional Error: 
        # Incorrect method name used for checking if the queue is empty Using len() instead of is_empty() to check if the queue is empty
        while len(self.message_list) > 0: # Fix: Change 'len(self.message_list) > 0' to 'self.queue.empty()'
            # Intentional Error:
            # Incorrect method used for receiving a message from the queue Using pop(0) instead of dequeue() to get a message
            message = self.message_list.pop(0)  # Fix: Change 'pop(0)' to 'dequeue()'
            print(f"Received message: {message}")

# Setting up the message queue
message_queue = MessageQueue()

# Sending messages to the queue
message_queue.send_message("Hello, World!")
message_queue.send_message("How are you?")
message_queue.send_message("Goodbye!")

# Receiving and displaying messages
print("\nReceived Messages:")
message_queue.receive_messages()

#########################
# 2) Challenge Solution #
#########################
# Python code for the "Set Manipulation" challenge problem

# Intentional Error:
# Incorrect method used for adding an element to the set
def add_element(s, element):
    s.adding(element)  # Fix: Change 'adding' to 'add'

# Intentional Error:
# Incorrect method used for removing an element from the set
def remove_element(s, element):
    s.removee(element)  # Fix: Change 'removee' to 'remove'

# Intentional Error:
# Incorrect method used for checking if an element is in the set
def check_element(s, element):
    if s.contains(element):  # Fix: Change 'contains' to 'in'
        print(f"{element} is in the set")
    else:
        print(f"{element} is not in the set")

# Example usage
my_set = {1, 2, 3, 4, 5}

add_element(my_set, 6)
remove_element(my_set, 3)
check_element(my_set, 2)

#########################
# 3) Challenge Solution #
#########################

# Intentional Error: 
# Incorrect method name for inserting a node in the Binary Search Tree
def add_node(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = add_node(root.left, key)  # Fix: Change 'add_node' to 'insert_node'
    else:
        root.right = add_node(root.right, key)  # Fix: Change  'add_node' to 'insert_node'
    return root

# Intentional Error: 
# Incorrect method name for performing in-order traversal
def traverse_tree_in_order(root):
    result = []
    if root:
        result = traverse_tree_in_order(root.left)  # Fix: Change 'traverse_tree_in_order' to 'in_order_traversal'
        result.append(root.key)
        result += traverse_tree_in_order(root.right)  # Fix: Change 'traverse_tree_in_order' to 'in_order_traversal'
    return result

# Intentional Error:
# Incorrect variable name for the root of the tree
tree_root = None # Fix: Change 'tree_root' to 'root'
keys = [50, 30, 70, 20, 40, 60, 80]

# Intentional Error:
# Incorrect method name for inserting nodes in the Binary Search Tree
for key in keys:
    tree_root = add_node(tree_root, key)  # Fix: Change 'add_node' to 'insert_node'

print("Incorrect In-order Traversal:", traverse_tree_in_order(tree_root))