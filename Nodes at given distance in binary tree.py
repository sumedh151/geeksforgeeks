#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def find_parent(self, node, parent, parent_map):
        if node is None:
            return
        parent_map[node] = parent
        self.find_parent(node.left, node, parent_map)
        self.find_parent(node.right, node, parent_map)

    def KDistanceNodes(self,root,target,k):
        # code here
        # return the sorted list all nodes at k distance from target
        from collections import deque
        parent_map = {}
        visited_map = {}
        self.find_parent(root, None, parent_map)
        q = deque()
        q.append(target)
        visited_map[target] = True
        dist_left = k
        while q and dist_left:
            for _ in range(len(q)):
                node = q.popleft()
                if parent_map[node] and parent_map[node] not in visited_map:
                    visited_map[parent_map[node]] = True
                    q.append(parent_map[node])
                if node.left and node.left not in visited_map:
                    visited_map[node.left] = True
                    q.append(node.left)
                if node.right and node.right not in visited_map:
                    visited_map[node.right] = True
                    q.append(node.right)
            dist_left-=1
        return sorted(list(map(lambda x: x.val , q)))