from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    # Time Complexity: O(n)
    def same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        return self.same_tree(p.right, q.right) and self.same_tree(p.left, q.left)

if __name__ == '__main__':
    s = Solution()
    tree1 = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    tree2 = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    print(s.same_tree(tree1, tree2))