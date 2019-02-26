# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 17:07:27
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-26 17:58:37

# 教程 https://time.geekbang.org/course/detail/130-67644
# 89% mem 72%


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = '#'

    def insert(self, word: 'str') -> 'None':
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for s in word:
            if s not in node:
                return False
            node = node.get(s)
        return self.end_of_word in node

    def startsWith(self, prefix: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for s in prefix:
            if s not in node:
                return False
            node = node.get(s)
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
