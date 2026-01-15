class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        if not arg_xdvx:
            return
        arg_ihhe.postorderTraversalHelper(arg_xdvx.left, arg_rcsn)
        arg_ihhe.postorderTraversalHelper(arg_xdvx.right, arg_rcsn)
        arg_rcsn.append(arg_xdvx.val)

    def func_bacg(arg_ihhe, arg_hqta):
        arg_rcsn = []
        arg_ihhe.postorderTraversalHelper(arg_hqta, arg_rcsn)
        return arg_rcsn
