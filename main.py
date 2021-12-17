class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class binTree:
    def __init__(self):
        self.root = None

    def addNewNode(self, data):
        if self.root is None:
            self.root = node(data)
            print(f"Val ({data}) added to bin tree")

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
                print(f"Val ({data}) added to bin tree")
                return
            elif data > bNode.data:
                bNode.right = node(data)
                print(f"Val ({data}) added to bin tree")
                return

    def inOrder(self, nod):
        if nod is None:
            return

        self.inOrder(nod.left)
        print(nod.data, end=' ')
        self.inOrder(nod.right)

    def recAddNode(self, data, nod=None):
        if self.root is None:
            self.root = node(data)
            print(f"Val ({data}) added to bin tree")
            return

        elif nod is None:
            nod = self.root

        if data < nod.data:
            if nod.left is None:
                nod.left = node(data)
                print(f"Val ({data}) added to bin tree")
                return

            self.recAddNode(data, nod.left)

        if data > nod.data:
            if nod.right is None:
                nod.right = node(data)
                print(f"Val ({data}) added to bin tree")
                return

            self.recAddNode(data, nod.right)

        if data == nod.data:
            print(f"Val ({data}) already in bin tree")


if __name__ == '__main__':
    tree = binTree()

    for i in range(10):
        tree.recAddNode(int(input()))

    tree.inOrder(tree.root)
