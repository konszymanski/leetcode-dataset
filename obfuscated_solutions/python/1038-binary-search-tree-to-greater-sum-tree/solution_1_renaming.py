class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.inorder_traversal = []
        arg_ihhe.inorder(arg_xdvx)
        arg_ihhe.inorder_traversal.reverse()
        arg_ihhe.replace_values(arg_xdvx)
        return arg_xdvx

    def func_rcsn(arg_ihhe, arg_xdvx):
        if arg_xdvx is None:
            return
        arg_ihhe.inorder(arg_xdvx.left)
        arg_ihhe.inorder_traversal.append(arg_xdvx.val)
        arg_ihhe.inorder(arg_xdvx.right)

    def func_bacg(arg_ihhe, arg_xdvx):
        if arg_xdvx is None:
            return
        arg_ihhe.replace_values(arg_xdvx.left)
        arg_ihhe.replace_values(arg_xdvx.right)
        var_hqta = 0
        for var_rgwu in arg_ihhe.inorder_traversal:
            if var_rgwu > arg_xdvx.val:
                var_hqta += var_rgwu
            else:
                break
        arg_xdvx.val += var_hqta
