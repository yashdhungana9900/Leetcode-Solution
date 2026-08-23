class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):

        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word):

        def dfs(index, node):

            if index == len(word):
                return node.is_end

            char = word[index]

            if char != ".":
                if char not in node.children:
                    return False

                return dfs(index + 1, node.children[char])

            # "." means any character
            for child in node.children.values():
                if dfs(index + 1, child):
                    return True

            return False

        return dfs(0, self.root)