from binary_tree import Node

# boring question in interview, i had to used yield to compelete
# although boring, but it is good for myself


def row_generator():
    i = yield None
    while 1:
        if i.lchild or i.rchild:
            i = yield i.lchild, i.rchild
        else:
            break


def get_element(root):

    if root.elem == None:
        return
    print root.elem
    row = row_generator()
    row.send(None)
    new_list = [root]
    for i in new_list:
        if i:
            left, right = row.send(i)
            print left, right
            new_list.append(left)
            new_list.append(right)

