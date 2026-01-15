class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = [0]
        arg_ihhe.bst_to_gst_helper(arg_xdvx, var_rcsn)
        return arg_xdvx

    def func_bacg(arg_ihhe, arg_xdvx, var_rcsn):
        if arg_xdvx is None:
            return
        arg_ihhe.bst_to_gst_helper(arg_xdvx.right, var_rcsn)
        var_rcsn[0] += arg_xdvx.val
        arg_xdvx.val = var_rcsn[0]
        arg_ihhe.bst_to_gst_helper(arg_xdvx.left, var_rcsn)
