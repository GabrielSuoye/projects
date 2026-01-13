# AVL Tree logic

if bf > 1 and key < root.left.key:
    return self.right_rotate(root)

if bf < -1 and key > root.right.key:
    return self.left_rotate(root)

if bf > 1 and key > root.left.key:
    root.left = self.left_rotate(root.left)
    return self.right_rotate(root)

if bf < -1 and key < root.right.key:
    root.right = self.right_rotate(root.right)
    return self.left_rotate(root)
