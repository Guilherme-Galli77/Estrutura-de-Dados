from os import system
system("cls")

# Create the node class
class BSTNode:
    def __init__(self, val=None):
        """
        Construtor of the BST class
        """
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        """
        Given a value, insert it on
        the BST 
        """
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
        
        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def preOrder(self, vals):
        """
        Contains the PreOrder algorithm
        implementation

        Returns
        -------
        List of values
        """
        if self.val is not None:
            vals.append(self.val)
        
        if self.left is not None:
            self.left.preOrder(vals)
        
        if self.right is not None:
            self.right.preOrder(vals)

        return vals

    def postOrder(self, vals):
        """
        Contains the PostOrder algorithm
        implementation

        Returns
        -------
        List of values
        """
        if self.left is not None:
            self.left.postOrder(vals)
        
        if self.right is not None:
            self.right.postOrder(vals)
        
        if self.val is not None:
            vals.append(self.val)
        
        return vals

    def inOrder(self, vals):
        """
        Contains the InOrder algorithm
        implementation

        Returns
        -------
        List of values
        """
        if self.left is not None:
            self.left.inOrder(vals)
        
        if self.val is not None:
            vals.append(self.val)

        if self.right is not None:
            self.right.inOrder(vals)
        
        return vals

    def exists(self, val):
        """
        Verify if a given value, val, 
        exists on a BST

        Returns
        -------
        True, if the value exists on 
        the BST;

        False, if the value do not exists 
        on the BST
        """
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)
        
        if self.right == None:
            return False
        return self.right.exists(val)

    def getMin(self):
        """
        Computes the minimum value of the BST.

        Returns
        -------
        The minimum value of the BST
        """
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    # Returns the ammount of nodes
    def countNodes(self):
        count = 1
        if self is None:
            return 0

        if self is not None:

            if self.left is not None:
                count += self.left.countNodes()
            if self.right is not None:
                count += self.right.countNodes()

        return count
    
    # Returns the mean values 
    def getMean(self):
        values = self.postOrder([])
        mean = sum(values)/len(values)
        return mean

   # Returns the high
    def GetHeight(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.GetHeight(root.left), self.GetHeight(root.right))

    # Returns the ammount of NULL's
    def getNumNulls(self): #TODO
        nulls = 0
        if (self.left is not None):
            self.left.countNodes()

        if (self.right is not None):
            self.right.countNodes()

        if (self.left is None):
            nulls += 1

        if (self.right is None):
            nulls += 1

        return nulls

    # Show values that are multiples of 2
    def ShowMultTwo(self):
        if (self.left is not None):
            self.left.ShowMultTwo()
        
        if (self.right is not None):
            self.right.ShowMultTwo()
        
        if ((self.val % 2) == 0):
            print(self.val, end='\t')

    # Returns sum of all the elements
    def sum(self):
        values = self.postOrder([])
        return sum(values)


def main():

    # Ex.1
    array = [3, 7, 8, 9, 10, 5]
    bst = BSTNode()
    for value in array:
        bst.insert(value)

    # Ex. 2
    k = 2
    bst.insert(k)

    # Ex. 3
    print("PreOrder:")
    print(bst.preOrder([]))
    
    # Ex. 4
    print("\nPostOrder")
    print(bst.postOrder([]))

    # Ex. 5
    print("\nInOrder")
    print(bst.inOrder([]))

    # Ex. 6
    print("\nVerify if k=2 exists on the BST:")
    print(bst.exists(2))

    print("\nVerify if k=15 exists on the BST:")
    print(bst.exists(15))

    # Ex. 7
    print("\nThe minimun value for this BST is:")
    print(bst.getMin())

    # Ex. 8
    print("\nThe ammount of nodes is:")
    print(bst.countNodes())

    # Ex. 9
    print("\nMean:")
    print(round(bst.getMean(), 2))
    
    # Ex. 10
    print("\nHeight:")
    print(bst.GetHeight(bst))

    # Ex. 11
    print("\nThe ammount of NULL's is:")
    print(bst.getNumNulls())

    # Ex. 12
    print("\nThe multiples of two are:")
    bst.ShowMultTwo()

    # Ex. 13
    print("\n\nSum:")
    print(bst.sum())
   


if __name__ == "__main__":
    main()