# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right and targetSum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, targetSum-root.val) + self.pathSum(root.right, targetSum-root.val)
        return [[root.val]+i for i in tmp]
