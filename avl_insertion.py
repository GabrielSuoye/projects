# Insertion of the new node into the tree

def insert(self, root, key):
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = self.insert(root.left, key)
    else:
        root.right = self.insert(root.right, key)

    root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

# Update the balance factor and balance the tree

bf = self.get_balance_factor(root)

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

return root
