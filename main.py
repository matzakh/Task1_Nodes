

# assumes that the tree only has one root, per its mathematical definition
def find_internal_nodes_num(tree):
    return len(set(tree)) - 1


if __name__ == '__main__':
    my_tree = [4, 4, 1, 5, -1, 4, 5]
    print(find_internal_nodes_num(my_tree))
    assert find_internal_nodes_num(my_tree) == 3

    my_tree = [5, -1, 4, 0, 3, 1]
    print(find_internal_nodes_num(my_tree))
    assert find_internal_nodes_num(my_tree) == 5

    my_tree = [0]
    print(find_internal_nodes_num(my_tree))
    assert find_internal_nodes_num(my_tree) == 0

    my_tree = [1, -1, 1, 1, 1]
    print(find_internal_nodes_num(my_tree))
    assert find_internal_nodes_num(my_tree) == 1

    my_tree = [1, -1, 1, 1, 1, 0, 5]
    print(find_internal_nodes_num(my_tree))
    assert find_internal_nodes_num(my_tree) == 3
