# David Hudson
# COMP 340

class TreeNode:
    def __init__(self, type, value, precedence):
        self.type = type
        self.value = value
        self.precedence = precedence

    parent = None
    l_child = None
    r_child = None


def get_precedence(type):
    precedence = 0
    if type == "PLUS" or type == "MINUS":
        precedence = 1
    elif type == "MULTIPLICATION" or type == "DIVISION":
        precedence = 2
    return precedence


def create_tree_node_list(tok_seq):
    tree_node_list = []
    x = 0
    for token in tok_seq:
        if token.type == "LPAREN":
            x += 4
        elif token.type == "RPAREN":
            x -= 4

        else:
            newNode = TreeNode(token.type, token.value, get_precedence(token.type) + x)
            tree_node_list.append(newNode)

    return tree_node_list


def parse(tok_seq):
    tree_node_list = create_tree_node_list(tok_seq)
    parsing(tree_node_list)
    root_node = find_root(tree_node_list)
    return root_node


def find_root(tree_node_list):
    root_node = None
    if len(tree_node_list) == 1:
        return tree_node_list[0]
    for node in tree_node_list:
        if node.parent is None and node.type != "DUMMY":
            root_node = node
            break

    return root_node


def parsing(tree_node_list):
    dummyNode = TreeNode("DUMMY", "", 0)
    tree_node_list.insert(0, dummyNode)
    tree_node_list.append(dummyNode)

    for index in range(len(tree_node_list)):
        node = tree_node_list[index]
        if node.type == "NUMBER":
            lOp = tree_node_list[index - 1]
            rOp = tree_node_list[index + 1]
            if rOp.precedence > lOp.precedence:
                # Right
                rOp.l_child = node
                node.parent = lOp
                if lOp.type != "DUMMY":
                    lOp.r_child = rOp
                    rOp.parent = lOp
            else:
                # Left
                lOp.r_child = node
                node.parent = lOp
                if rOp.type != "DUMMY":
                    while lOp.parent is not None:
                        if lOp.parent.precedence < rOp.precedence:
                            break
                        lOp = lOp.parent
                    if lOp.parent is not None:
                        lOp.parent.r_child = rOp
                        rOp.parent = lOp.parent
                    rOp.l_child = lOp
                    lOp.parent = rOp

                if lOp.type == "DUMMY" and rOp.type == "DUMMY":
                    tree_node_list.clear()
                    tree_node_list.append(node)
                    break


def print_tree(root_node):
    if root_node.l_child is None and root_node.r_child is None:
        print(root_node.value, end="")
    else:
        print("(", end="")
        print_tree(root_node.l_child)
        print(root_node.value, end="")
        print_tree(root_node.r_child)
        print(")", end="")
