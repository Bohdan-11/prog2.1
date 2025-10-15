

def gen_bin_tree(height = 3, root = 1):
    
    
    if height == 1:
        return  {'root': root, 'left': None, 'right': None}

    left_child = root + 1
    right_child = root - 1

    return {
        'root': root,
        'left': gen_bin_tree(height - 1, left_child),
        'right': gen_bin_tree(height - 1, right_child)
    }

tree = gen_bin_tree(3)
print(tree)

        
