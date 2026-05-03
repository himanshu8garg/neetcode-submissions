# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        l = []
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            m = []
            for i in range (len(queue)):
                curr = queue.popleft()
                m.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            l.append(m)
        return l
