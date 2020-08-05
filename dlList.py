from dlNode import Node

class DubLinkList:
    def __init__(self):
        self.start_node = None
        ## set tail node ##
        self.end_node = None
    def addNode_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            self.end_node = self.start_node
        else:
            print("Error: List is not empty")

    def insert_new_node_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start = new_node
            print("Node inserted to front of list")
            return
        new_node = Node(data)
        new_node.nRef = self.start_node
        self.start_node.pRef = new_node
        self.start_node = new_node
    
    def insert_node_start(self, node):
        if self.start_node is None:
            new_node = Node(data)
            self.start = new_node
            print("Node inserted to front of list")
            return
        
        node.nRef = self.start_node
        self.start_node.pRef = node
        self.start_node = node

    def insert_node_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nRef is not None:
            n = n.nRef
        new_node = Node(data)
        n.nRef = new_node
        new_node.pRef = n
        ## add end_node
        self.end_node = new_node

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nRef
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pRef = n
                new_node.nRef = n.nRef
                if n.nRef is not None:
                    n.nRef.prev = new_node
                n.nRef = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nRef
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nRef = n
                new_node.pRef = n.pRef
                if n.pRef is not None:
                    n.pRef.nRef = new_node
                n.pRef = new_node

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " -> ")
                n = n.nRef

    def traverse_list_array(self):
        self_list = []
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                self_list.append(n.item)
                n = n.nRef
        return self_list

    def handle_delete(self, cur_node, actual_moves=None):
        if cur_node.pRef == None:    
            self.delete_at_start()
        elif cur_node.nRef == None:
            self.delete_at_end()
        else:
            self.delete_element_by_value(actual_moves) 

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nRef is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nRef
        self.start_prev = None


    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nRef is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nRef is not None:
            n = n.nRef
        n.pRef.nRef = None

    def delete_element_by_value(self, actual_moves):
        n = self.start_node
        for m in range(0, actual_moves):
            n = n.nRef
        if n.nRef is not None:
            n.pRef.nRef = n.nRef
            n.nRef.pRef = n.pRef
        else:
            print("Element not found")
    
    def get_size(self):
        res = 1
        n = self.start_node
        while (n.nRef != None):
            res = res + 1
            n = n.nRef
        return res