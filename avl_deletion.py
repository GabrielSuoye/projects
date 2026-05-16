# AVL Tree Deletion

def delete(self, root, key):
    if not root:
        return root
    elif key < root.key:
        root.left = self.delete(root.left, key)
    elif key > root.key:
        root.right = self.delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp

        # Find inorder successor
        
        temp = self.get_min_node(root.right)
        root.key = temp.key
        root.right = self.delete(root.right, temp.key)

    # Rebalancing the AVL Tree
    
    if bf > 1 and self.get_balance_factor(root.left) >= 0:
        return self.right_rotate(root)

    if bf < -1 and self.get_balance_factor(root.right) <= 0:
        return self.left_rotate(root)

    if bf > 1 and self.get_balance_factor(root.left) < 0:
        root.left = self.left_rotate(root.left)
        return self.right_rotate(root)

    if bf < -1 and self.get_balance_factor(root.right) > 0:
        root.right = self.right_rotate(root.right)
        return self.left_rotate(root)
