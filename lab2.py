

class Element():
    def __init__(self, key ,value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ": " + str(self.value)

class Node:
    def __init__(self, element: Element, left, right):
        self.element = element
        self.left = left
        self.right = right

    def __str__(self):
        whole = ""
        left = str(self.left)
        if left != "None":
            whole += left + "\n"
        whole += str(self.element) + "\n"
        right = str(self.right)
        if right != "None":
            whole += right + "\n"
        return whole
        


class SymbolTable():
    
    def __init__(self):
        """Initializes the symbol table"""
        self.next_index = 0
        self.base: Node = None

    def position(self, key):
        """Searches for the item, if it does not exist, add it"""
        
        # if collection empty
        if self.base is None:
            index = self.next_index
            self.next_index += 1
            self.base = Node(Element(key,index),None,None)
            return index

        # search
        node = self.base
        while node.element.key != key:
            if key < node.element.key:
                # left
                if node.left is not None:
                    # go on
                    node = node.left
                else:
                    # add it
                    index = self.next_index
                    self.next_index += 1
                    node.left = Node(Element(key,index),None,None)
                    return index
            else:
                # right
                if node.right is not None:
                    # go on
                    node = node.right
                else:
                    # add it
                    index = self.next_index
                    self.next_index += 1
                    node.right = Node(Element(key,index),None,None)
                    return index
        # found it
        return node.element.value

    def __str__(self):
        if self.base is None:
            return "[]"
        return "[\n" + str(self.base) + "]"