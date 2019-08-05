from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        pass


solution = Solution()
assert solution.buildTree(
    inorder=[9, 3, 15, 20, 7],
    postorder=[9, 15, 7, 20, 3]) == [3, 9, 20, None, None, 15, 7]
