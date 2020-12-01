# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# BFS solution
def depthSum(self, nestedList):
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """
    depth, ret = 1, 0
    while nestedList:
        ret += depth * sum([x.getInteger() for x in nestedList if x.isInteger()])
        nestedList = sum([x.getList() for x in nestedList if not x.isInteger()], [])
        depth += 1
    return ret


# Recursion soultion
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def level_sum(current_level, nestedList):
            res = 0
            for itm in nestedList:
                if itm.isInteger():
                    res += current_level * itm.getInteger()
                else:
                    res += level_sum(current_level + 1, itm.getList())
            return res

        current_level = 1
        return level_sum(current_level, nestedList)