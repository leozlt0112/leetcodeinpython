class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
        
class Queue:
    def __init__(self,value):
        newNode = Node(value)
        self.first = newNode
        self.height = 1
    ## WRITE QUEUE CONSTRUCTOR HERE ##
    #                                #
    #                                #
    #                                #
    #                                #
    ##################################

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next




my_queue = Queue(4)

my_queue.print_queue()



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""