class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def 
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
        
# class Stack:
    ## WRITE STACK CONSTRUCTOR HERE ##
    #                                #
    #                                #
    #                                #
    #                                #
    ##################################




my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)
my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""