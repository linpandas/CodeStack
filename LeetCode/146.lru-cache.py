#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30204
#
# [146] LRU 缓存
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Node:
    __slots__ = "prev", "next", "key", "value"
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy_head = Node()
        self.dummy_head.prev = self.dummy_head
        self.dummy_head.next = self.dummy_head
        self.key2node = dict()
    
    def get_node(self, key):
        # 给定key，将node放到“最顶层”，并返回node
        if key not in self.key2node:
            return None
        node = self.key2node[key]
        self.remove(node)
        self.push_front(node)
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node: # 有这本书，更新值后返回
            node.value = value
            return
        # 没这本书
        self.key2node[key] = node = Node(key, value)
        self.push_front(node)
        if len(self.key2node) > self.capacity:
            back_node = self.dummy_head.prev
            del self.key2node[back_node.key]
            self.remove(back_node)
    
    def remove(self, x: Node):
        # 移除x
        x.prev.next = x.next
        x.next.prev = x.prev
    
    def push_front(self, x: Node):
        # 将x放到“最顶层”
        x.prev = self.dummy_head
        x.next = self.dummy_head.next
        x.prev.next = x
        x.next.prev = x
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



