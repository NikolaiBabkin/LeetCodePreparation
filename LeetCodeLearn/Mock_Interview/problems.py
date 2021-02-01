"""
Problems list

Easy:   169. Majority Element
        1022. Sum of Root To Leaf Binary Numbers

Medium: 1265. Print Immutable Linked List in Reverse
        669. Trim a Binary Search Tree

Hard:

"""


class ProblemSolution(object):
    def __init__(self):
        pass


class TrimBST(ProblemSolution):
    """
    669. Trim a Binary Search Tree
    https://leetcode.com/problems/trim-a-binary-search-tree/

    Given the root of a binary search tree and the lowest and highest boundaries as low and high,
    trim the tree so that all its elements lies in [low, high].
    Trimming the tree should not change the relative structure of the elements
    that will remain in the tree (i.e., any node's descendant should remain a descendant).
    It can be proven that there is a unique answer.
    Return the root of the trimmed binary search tree.
    Note that the root may change depending on the given bounds.

    Example 1
    Input:
       1
     /  \
    0    2
    low = 1, high = 2

    Output:
    1
     \
      2

    Example 2
    Input:
       3
      /  \
     0    4
      \
       2
      /
    1
    low = 1, high = 2

    Output:
        3
       /
      2
     /
    1

    Constraints:

    - The number of nodes in the tree in the range [1, 10E6].
    - 0 <= Node.val <= 10E6
    - The value of each node in the tree is unique.
    - root is guaranteed to be a valid binary search tree.
    - 0 <= low <= high <= 10E6

    """
    def __init__(self):
        super().__init__()

    def trim_bst(self, root, low, high):
        def is_lies_in_boundaries(node):
            return low <= node.val <= high

        def find_next_node(node):
            while node and not is_lies_in_boundaries(node):
                if node.val < low:
                    node = node.right
                else:
                    node = node.left
            return node

        root = find_next_node(root)
        if root:
            stack = [root]
            while stack:
                node = stack.pop(-1)
                if node.right:
                    node_right = find_next_node(node.right)
                    node.right = node_right
                    if node_right:
                        stack.append(node.right)
                if node.left:
                    node_left = find_next_node(node.left)
                    node.left = node_left
                    if node_left:
                        stack.append(node.left)

        return root



class MajorityElement(ProblemSolution):
    """
    169. Majority Element
    https://leetcode.com/problems/majority-element/
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.

    Example 1:
    Input: nums = [3,2,3]
    Output: 3

    Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

    Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -231 <= nums[i] <= 231 - 1

    The task should be solved with TC = O(n) ans SC = O(1)
    Hints:
    1. Look at this problem as at voting results calculation
    2. What if we have just 2 candidates
    3. Can we calculate the result for 2 candidates using just one variable?
    4. What about 3 candidates

    Follow up:
    1. What if we don't now that the majority element always exists in the array?
    """
    def __init__(self):
        super().__init__()

    def majority_element_1(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n*2)
        Space Complexity: O(1)
        """
        majority_min_count = len(nums) // 2
        for current in nums:
            count = sum(1 for num in nums if current == num)
            if count > majority_min_count:
                return current

    def majority_element_2(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        counts = dict()
        majority_min_count = len(nums) // 2
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] > majority_min_count:
                return num

    def majority_element_3(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n*log(n))
        Space Complexity: O(1)
        """
        nums.sort()
        return nums[len(nums) // 2]

    def majority_element_4(self, nums: list[int]) -> int:
        """
        Boyer-Moore Voting Algorithm
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current_elem = nums[0]
        count = 1
        for num in nums:
            if count == 0:
                current_elem = num
                count += 1
            else:
                if current_elem == num:
                    count += 1
                else:
                    count -= 1
        return current_elem


class ReverseImmutableLinkedList(ProblemSolution):
    """
    1265. Print Immutable Linked List in Reverse
    https://leetcode.com/problems/print-immutable-linked-list-in-reverse/
    
    You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:

    ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
    You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):

    ImmutableListNode.printValue(): Print value of the current node.
    ImmutableListNode.getNext():    Return the next node.
    
    The input is only given to initialize the linked list internally.
    You must solve this problem without modifying the linked list.
    In other words, you must operate the linked list using only the mentioned APIs.
    
    
    Example 1:
    Input: head = [1,2,3,4]
    Output: [4,3,2,1]
    
    Example 2:
    Input: head = [0,-4,-1,3,-5]
    Output: [-5,3,-1,-4,0]
    
    Example 3:
    Input: head = [-2,0,6,4,4,-6]
    Output: [-6,4,4,6,0,-2]
     
    
    Constraints:
    The length of the linked list is between [1, 1000].
    The value of each node in the linked list is between [-1000, 1000].
    
    Hints:
    Can we improve iterative(stack) solution in case of memory capacity?
    What if we will store each second element in stack? What SC would be in this case: sum(2 + n/2)?
    What if we will store each k elem in stack? SC: k + n / k?
    d(k + n / k)/dk == 0


    Follow up:
    Could you solve this problem in:
    1. Constant space complexity?
    2. Linear time complexity and less than linear space complexity?
    """

    def __init__(self):
        super().__init__()

    def print_linked_list_reverse_1(self, head: 'ImmutableListNode') -> None:
        """
        Solution with stack approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        while head:
            stack.append(head)
            head = head.getNext()
        for node in stack[::-1]:
            print(node.printValue())

    def print_linked_list_reverse_2(self, head: 'ImmutableListNode') -> None:
        """
        Solution with recursion approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if head.getNext() is None:
            head.printValue()
        else:
            self.print_linked_list_reverse_2(head.getNext())
            head.printValue()

    def print_linked_list_reverse_3(self, head: 'ImmutableListNode') -> None:
        """
        Solution with recursion approach
        Time Complexity: O(n**2)
        Space Complexity: O(1)
        """
        node = head
        list_len = 0
        while node:
            list_len += 1
            node = node.getNext()

        for i in range(list_len - 1, -1, -1):
            node = head
            for _ in range(i):
                node = node.getNext()
            node.printValue()

    def print_linked_list_reverse_4(self, head: 'ImmutableListNode') -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(n^(1/2))
        """

        def helper(head: 'ImmutableListNode', stop_node) -> None:
            """
            Time Complexity: O(n)
            Space Complexity: O(n)
            """
            res = []
            node = head
            while node != stop_node:
                res.append(node)
                node = node.getNext()
            while res:
                node = res.pop(-1)
                node.printValue()


        size = 0
        node = head
        while node:
            size += 1
            node = node.getNext()

        step = int(size ** 0.5)
        sub_heads = [0] * (step)
        sub_heads[0] = head
        for i in range(1, len(sub_heads)):
            node = sub_heads[i - 1]
            cnt = step
            while cnt:
                if node.getNext():
                    node = node.getNext()
                    cnt -= 1
                else:
                    break
            if cnt == 0:
                sub_heads[i] = node

        stop_node = None
        for node in sub_heads[::-1]:
            helper(node, stop_node)
            stop_node = node


class SumRootToLeafBinaryNumbers(ProblemSolution):
    """
    1022. Sum of Root To Leaf Binary Numbers
    https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

    You are given the root of a binary tree where each node has a value 0 or 1.
    Each root-to-leaf path represents a binary number starting with the most significant bit.
    For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

    For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

    Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

    Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    Node.val is 0 or 1.

    Hints to find Morris algorithm:
    What if we have tree like
        1
      /   \
    1       0
    Can we without stack, recursion, without any memorisation any additional memory, just for result, solve it?
    We can modify tree in the way we can return late it to initial.
    We can add links and then delete them.
    ...

    Follow up:
    Can we do in on constant time?
    """

    def __init__(self):
        super().__init__()

    def sumRootToLeaf_iterative(self, root: TreeNode) -> int:
        """
        Iterative DFS
        Time Complexity: O(n)
        Space Complexity: O(H)
        """
        res = 0
        stack = [(root, root.val)]
        while stack:
            node, number = stack.pop()
            if node.right:
                number_new = (number << 1) | node.right.val
                stack.append((node.right, number_new))
            if node.left:
                number_new = (number << 1) | node.left.val
                stack.append((node.left, number_new))
            if node.left is None and node.right is None:
                res += number
        return res

    def sumRootToLeaf_recursive(self, root: TreeNode) -> int:
        """
        Recursive DFS
        Time Complexity: O(n)
        Space Complexity: O(H)
        """
        def recursion_sum(node, number):
            nonlocal res
            if node.left is None and node.right is None:
                res += number
            else:
                if node.left:
                    number_new = (number << 1) | node.left.val
                    recursion_sum(node.left, number_new)
                if node.right:
                    number_new = (number << 1) | node.right.val
                    recursion_sum(node.right, number_new)

        res = 0
        recursion_sum(root, root.val)
        return res

    def sumRootToLeaf_morris(self, root: TreeNode) -> int:
        """
        Recursive DFS
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = number = 0
        current = root
        while current:
            if current.left:
                predecessor = current.left
                steps = 1
                while predecessor.right and predecessor.right is not current:
                    predecessor = predecessor.right
                    steps += 1

                if predecessor.right is None:
                    number = (number << 1) | current.val
                    predecessor.right = current
                    current = current.left

                else:
                    if predecessor.left is None:
                        res += number

                    for _ in range(steps):
                        number >>= 1
                    predecessor.right = None
                    current = current.right

            else:
                number = (number << 1) | current.val
                if current.right is None:
                    res += number
                current = current.right

        return res