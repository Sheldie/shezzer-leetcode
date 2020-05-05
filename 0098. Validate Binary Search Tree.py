# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import queue
from typing import List


# 98. 验证二叉搜索树
# medium
# 树 dfs

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createTree(ls: List) -> TreeNode:
    size = len(ls) // 2
    nodes = queue.Queue()
    root = TreeNode(ls[0])
    nodes.put(root)
    for idx in range(size):
        node = nodes.get()
        left = idx * 2 + 1
        right = idx * 2 + 2
        if ls[left] != 'null':
            node.left = TreeNode(ls[left])
            nodes.put(node.left)
        else:
            nodes.put(None)
        if ls[right] != 'null':
            node.right = TreeNode(ls[right])
            nodes.put(node.right)
        else:
            nodes.put(None)
    return root


class Solution:
    # Solution
    # 中序遍历
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        last = float('-inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if last < root.val:
                last = root.val
            else:
                return False
            if root.right:
                root = root.right
            else:
                root = None
        return True


if __name__ == '__main__':
    ls = [5, 1, 4, 'null', 'null', 3, 6]
    # ls = [2, 1, 3]
    root = createTree(ls)
    print(Solution().isValidBST(root))
