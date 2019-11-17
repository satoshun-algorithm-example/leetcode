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
        values = []
        while nodes:
            new_nodes = []
            for node in nodes:
                if node.left:
                    node.left.value = node.value * 2 + 1
                    values.append(node.value * 2 + 1)
                    new_nodes.append(node.left)

                if node.right:
                    node.right.value = node.value * 2 + 2
                    values.append(node.value * 2 + 2)
                    new_nodes.append(node.right)
            nodes = new_nodes

        self.values = values
        self.root = root

    def find(self, target: int) -> bool:
        start = 0
        end = len(self.values)
        while start < end:
            mid = (end + start) // 2
            if self.values[mid] == target:
                return True
            elif self.values[mid] > target:
                end = mid
            else:
                start = mid + 1

        return False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
