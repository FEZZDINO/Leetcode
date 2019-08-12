"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        height = 0
        print(root)
        for node in root.children:
            height = max(self.maxDepth(node),height)
        return height+1