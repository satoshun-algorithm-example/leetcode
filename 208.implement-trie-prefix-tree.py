#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                new_node = Node(c)
                node.children[c] = new_node
                node = new_node
        node.is_leaf = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_leaf

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_leaf = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
