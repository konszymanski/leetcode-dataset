class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_ayzf[var_wnki]:
        var_hqta = []
        if arg_xdvx is None:
            return var_hqta
        var_rgwu = None
        var_wrnh = []
        while arg_xdvx is not None or var_osiz(var_wrnh) > 0:
            if arg_xdvx is not None:
                var_wrnh.append(arg_xdvx)
                arg_xdvx = arg_xdvx.left
            else:
                arg_xdvx = var_wrnh[-1]
                if arg_xdvx.right is None or arg_xdvx.right == var_rgwu:
                    var_hqta.append(arg_xdvx.val)
                    var_wrnh.pop()
                    var_rgwu = arg_xdvx
                    arg_xdvx = None
                else:
                    arg_xdvx = arg_xdvx.right
        return var_hqta
