class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_osiz:
        if not arg_xdvx.left and not arg_xdvx.right:
            return arg_xdvx.val != 0
        var_hqta = arg_ihhe.evaluateTree(arg_xdvx.left)
        var_rgwu = arg_ihhe.evaluateTree(arg_xdvx.right)
        if arg_xdvx.val == 2:
            var_wrnh = var_hqta or var_rgwu
        else:
            var_wrnh = var_hqta and var_rgwu
        return var_wrnh
