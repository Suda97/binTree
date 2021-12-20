class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class binTree:
    def __init__(self):
        self.root = None

    # linear adding to tree
    def addNewNode(self, data):
        if self.root is None:
            self.root = node(data)

        else:
            pNode = self.root
            bNode = None

            while pNode:
                bNode = pNode
                if data < pNode.data:
                    pNode = pNode.left
                elif data > pNode.data:
                    pNode = pNode.right
                else:
                    print(f"Val ({data}) already in bin tree")
                    return

            if data < bNode.data:
                bNode.left = node(data)
                return
            elif data > bNode.data:
                bNode.right = node(data)
                return

    # recursive printing of tree in order
    def inOrder(self, nod):
        if nod is None:
            return

        self.inOrder(nod.left)
        print(nod.data, end=' ')
        self.inOrder(nod.right)

    # recursive adding to tree
    def recAddNode(self, data, nod=None):
        if self.root is None:
            self.root = node(data)
            return

        elif nod is None:
            nod = self.root

        if data < nod.data:
            if nod.left is None:
                nod.left = node(data)
                return

            self.recAddNode(data, nod.left)

        if data > nod.data:
            if nod.right is None:
                nod.right = node(data)
                return

            self.recAddNode(data, nod.right)

        if data == nod.data:
            print(f"Val ({data}) already in bin tree")

    def recInvert(self, nod):
        if nod is None:
            return

        self.recInvert(nod.left)
        self.recInvert(nod.right)

        tmp = nod.left
        nod.left = nod.right
        nod.right = tmp

    def height(self, nod):
        if nod is None:
            return 0

        leftHeight = self.height(nod.left)
        rightHeight = self.height(nod.right)

        return max(leftHeight, rightHeight) + 1


if __name__ == '__main__':
    tree = binTree()
    arr = [10, 2, 13, 1, 5, 12, 14, 0, 11, 23]

    for i in arr:
        tree.recAddNode(i)

    tree.inOrder(tree.root)
    print("")
    tree.recInvert(tree.root)
    tree.inOrder(tree.root)
    print(f"\nHeight of tree: {tree.height(tree.root)}")
