# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:
    def __init__(self, root: TreeNode):
        root.value = 0
        nodes = [root]
        while nodes:
            new_nodes = []
            for node in nodes:
                if node.left:
                    node.left.value = node.value * 2 + 1
                    new_nodes.append(node.left)

                if node.right:
                    node.right.value = node.value * 2 + 2
                    new_nodes.append(node.right)
            nodes = new_nodes

        self.root = root

    def find(self, target: int) -> bool:
        nodes = [self.root]
        while nodes:
            new_nodes = []
            for node in nodes:
                if node.value == target:
                    return True
                if target < node.value:
                    continue
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)

            nodes = new_nodes

        return False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
