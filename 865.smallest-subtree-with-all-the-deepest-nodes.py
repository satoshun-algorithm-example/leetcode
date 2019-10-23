#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        deepest_node_map = {}

        def find_deepest_nodes(node, parent, depth):
            if not node:
                return

            node.parent = parent
            deepest_node_map[depth] = deepest_node_map.get(depth, []) + [node]
            find_deepest_nodes(node.right, node, depth + 1)
            find_deepest_nodes(node.left, node, depth + 1)

        find_deepest_nodes(root, None, 0)

        deepest_nodes = deepest_node_map[max(deepest_node_map)]

        if len(deepest_nodes) == 1:
            return deepest_nodes[0]

        while True:
            parent = []
            for node in deepest_nodes:
                parent.append(node.parent)

            check = parent[0]
            for node in parent:
                if check != node:
                    check = None
                    break
            if check:
                return check
            deepest_nodes = parent

# @lc code=end
