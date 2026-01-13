def left_rotate(self, node):
    B = node.right 
    Y = B.left

    B.left = node
    node.right = Y 

    node.height = 1 + max(self.get_height(node, left), self.get_height(node.right))
    B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))

    return B 
