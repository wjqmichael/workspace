# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        def gen_sub_tree(lst):
            if not len(lst): return [None]
            rt = []
            for i in xrange(len(lst)):
                left = gen_sub_tree(lst[0:i])
                right = gen_sub_tree(lst[i+1:])
                for l in left:
                    for r in right:
                        node = TreeNode(lst[i])
                        node.left = l
                        node.right = r
                        rt.append(node)
            return rt
        return gen_sub_tree(range(1, n + 1))

s = Solution()
print s.generateTrees(3)