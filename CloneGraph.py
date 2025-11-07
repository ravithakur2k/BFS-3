"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

# Time complexity: O(V+E) as we are traversing through all the vertex and edges. Space is also same as using the queue data structure with map. The space is O(V)
# The intuition here is to create a copy of the node and store it in hashmap and use that to create neighbors whenever required.
class Solution:
    def cloneGraphBFS(self, node: Optional['Node']) -> Optional['Node']:

        if not node: return node

        queue = deque()
        queue.append(node)
        hashmap = {}
        visit = set()
        visit.add(node)
        while queue:
            currNode = queue.popleft()
            if currNode not in hashmap:
                hashmap[currNode] = Node(currNode.val)
            for nei in currNode.neighbors:
                if nei not in hashmap:
                    hashmap[nei] = Node(nei.val)
                if nei not in visit:
                    queue.append(nei)
                    visit.add(nei)
                hashmap[currNode].neighbors.append(hashmap[nei])

        return hashmap[node]

    # The same can be achieved using a DFS approach as well. 
    def cloneGraphDFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node

        self.map = {}
        self.dfs(node)
        return self.map[node]

    def dfs(self, curr):

        if curr not in self.map:
            self.map[curr] = Node(curr.val)

        copyCurr = self.map[curr]
        for nei in curr.neighbors:
            if nei not in self.map:
                self.dfs(nei)
            copyCurr.neighbors.append(self.map[nei])