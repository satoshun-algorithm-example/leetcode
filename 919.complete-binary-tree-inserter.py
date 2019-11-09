#
# @lc app=leetcode id=919 lang=python3
#
# [919] Complete Binary Tree Inserter
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.tree = [root]

        for node in self.tree:
            if node.left:
                self.tree.append(node.left)
            if node.right:
                self.tree.append(node.right)

    def insert(self, v: int) -> int:
        n = len(self.tree) - 1
        last = TreeNode(v)
        self.tree.append(last)
        if n % 2 == 0:
            self.tree[n // 2].left = last
        else:
            self.tree[n // 2].right = last

        return self.tree[n // 2].val

    def get_root(self) -> TreeNode:
        return self.tree[0]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
# @lc code=end
