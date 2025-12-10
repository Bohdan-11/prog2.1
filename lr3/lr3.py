

def gen_bin_tree(height = 4, root = 8):
    
    
    if height == 1:
        return  {'root': root, 'left': None, 'right': None}

    left_child = root + (root / 2)
    right_child = root * root

    return {
        'root': root,
        'left': gen_bin_tree(height - 1, left_child),
        'right': gen_bin_tree(height - 1, right_child)
    }

tree = gen_bin_tree()
print(tree)

        
