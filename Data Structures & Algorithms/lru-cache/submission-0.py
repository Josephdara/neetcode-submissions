class DLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.capacity = capacity
        #Recency is L -> R, least -> Most
        self.least ,self.most = DLNode(0,0), DLNode(0,0)
        self.least.next, self.most.prev = self.most, self.least

    def addx(self, key, node):
        node.prev , node.next = self.most.prev , self.most
        self.most.prev.next, self.most.prev =  node, node
        self.cache_dict[key] = node
        
    def subx(self,key, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache_dict[node.key]

        

    def get(self, key: int) -> int:
        if key in self.cache_dict:
            #update vals position
            node = self.cache_dict[key]
            self.subx(key,node)
            self.addx(key, node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        node = DLNode(key,value)
        if key in self.cache_dict:
            self.subx(key, self.cache_dict[key])
        self.addx(key, node)

        if len(self.cache_dict) > self.capacity:
            last_valid_node = self.least.next
            self.subx(last_valid_node.key,last_valid_node)