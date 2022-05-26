from src.easy import same_tree_100




def test_same_tree():
    s = same_tree_100.Solution()
    tree1 = same_tree_100.TreeNode(1, same_tree_100.TreeNode(2, None, None), same_tree_100.TreeNode(3, None, None))
    tree2 = same_tree_100.TreeNode(1, same_tree_100.TreeNode(2, None, None), same_tree_100.TreeNode(3, None, None))
    assert s.same_tree(tree1, tree2) == True
