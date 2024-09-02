class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.past_node = None
        
    def set_next_node(self, node):
        self.next_node = node

    def set_past_node(self, node):
        self.past_node = node

    def set_node_value(self, value):
        self.value = value
    
    


class DobleLinkedList:
    def __init__(self, enter_list = []):
        self.head = None
        for i in enter_list:
            self.push(i)
    def push(self, num):
        cur_node = Node(num)
        if not self.head:
            self.head = cur_node
        else:
            self.tail.set_next_node(cur_node)
            cur_node.set_past_node(self.tail)
        self.tail = cur_node

    def search_meaning(self, num):
        cur_node = self.head
        while cur_node:
            if cur_node.value == num:
                return True
            cur_node = cur_node.next_node
        return False
    
    def search_index(self, index):
        cur_node = self.head
        for i in range(index):
            cur_node = cur_node.next_node
        return cur_node.value
    
    def pop_meaning(self, num):
        cur_node = self.head
        while cur_node:
            if cur_node.value == num:
                self.dellete(cur_node)
                break
            cur_node = cur_node.next_node

    def pop_index(self, index):
        cur_node = self.head
        for i in range(index):
            cur_node = cur_node.next_node
        self.dellete(cur_node)

    def dellete(self, cur_node):
        next_node = cur_node.next_node
        prev_node = cur_node.past_node
        if not prev_node:
            next_node.set_past_node(None)
            self.head = next_node
        elif not next_node:
            prev_node.set_next_node(None)
        else:
            next_node.set_past_node(prev_node)
            prev_node.set_next_node(next_node)
    
    def exit(self):
        x = self.head
        answer = ''
        while x:
            answer += str(x.value) + ' -> ' 
            x = x.next_node
        return answer[:-4]





lst = DobleLinkedList()
lst.push(3)
lst.push(4)
print(lst.exit())
lst.pop_index (0)
lst.pop_meaning(21)
print(lst.exit())
