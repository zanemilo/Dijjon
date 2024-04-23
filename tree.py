# Dijjon tree
# Developed & designed by: Zane M Deso
# Purpose: This will be the class for the tree that will act as an abstract class for other trees as needed such asmaps, dungeons, choices, etc.

class Tree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def insertTree(self, data):
        if data < self.root:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insertTree(data)
        else:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insertTree(data)

    def deleteNode(self, data):
        if data < self.root:
            if self.left:
                self.left = self.left.deleteNode(data)
        elif data > self.root:
            if self.right:
                self.right = self.right.deleteNode(data)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_larger_node = self.right.findMin()
                self.root = min_larger_node.root
                self.right = self.right.deleteNode(min_larger_node.root)
        return self

    def findMin(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.root

    def findMax(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.root

    def size(self):
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return 1 + left_size + right_size

    def total(self):
        left_total = self.left.total() if self.left else 0
        right_total = self.right.total() if self.right else 0
        return self.root + left_total + right_total

    def traverseBreadthFirst(self):
        queue = [self]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.root)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def traverseDepthFirst(self):
        result = []
        if self.left:
            result.extend(self.left.traverseDepthFirst())
        result.append(self.root)
        if self.right:
            result.extend(self.right.traverseDepthFirst())
        return result


# tree = Tree(10)  # Start with a more central root for a balanced example
# for x in range(15):
#     if x != 10:  # Exclude the root value to avoid duplication
#         tree.insertTree(x)

# # Print the original tree structure
# print("Original Tree (BFS):", tree.traverseBreadthFirst())

# # Deleting the node and printing results
# tree.deleteNode(1)  # Deleting a non-root, simpler scenario
# print("Tree after deleting 1 (BFS):", tree.traverseBreadthFirst())

