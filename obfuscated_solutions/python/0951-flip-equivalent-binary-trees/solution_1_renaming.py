class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_osiz:
        if not arg_xdvx and not arg_rcsn:
            return True
        if not arg_xdvx or not arg_rcsn:
            return False
        if arg_xdvx.val != arg_rcsn.val:
            return False
        var_rgwu = arg_ihhe.flipEquiv(arg_xdvx.left, arg_rcsn.left
            ) and arg_ihhe.flipEquiv(arg_xdvx.right, arg_rcsn.right)
        var_wrnh = arg_ihhe.flipEquiv(arg_xdvx.left, arg_rcsn.right
            ) and arg_ihhe.flipEquiv(arg_xdvx.right, arg_rcsn.left)
        return var_rgwu or var_wrnh
