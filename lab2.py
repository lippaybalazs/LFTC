

class Element():
    def __init__(self, key ,value):
        self.key = key
        self.value = value

class Node:
    def __init__(self, element: Element, left, right):
        self.element = element
        self.left = left
        self.right = right

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


        
stI = SymbolTable()
print(stI.position("c"))
print(stI.position("a"))
print(stI.position("d"))
print(stI.position("b"))
print(stI.position("e"))
print(stI.position("c"))
print(stI.position("a"))
print(stI.position("d"))
print(stI.position("b"))
print(stI.position("e"))

print()

stC = SymbolTable()
print(stC.position("1"))
print(stC.position("2"))
print(stC.position("dasd"))
print(stC.position("b12"))
print(stC.position("ez"))
print(stC.position("1"))
print(stC.position("2"))
print(stC.position("dasd"))
print(stC.position("b12"))
print(stC.position("ez"))