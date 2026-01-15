class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = []
        arg_ihhe.helper(arg_xdvx, var_rcsn)
        return var_rcsn

    def func_bacg(arg_ihhe, arg_xdvx, var_rcsn):
        if arg_xdvx is not None:
            arg_ihhe.helper(arg_xdvx.left, var_rcsn)
            var_rcsn.append(arg_xdvx.val)
            arg_ihhe.helper(arg_xdvx.right, var_rcsn)
