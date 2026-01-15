class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_egyk[var_dcmd]:

        def func_hqta(arg_rgwu, arg_wrnh):
            if not arg_rgwu:
                return
            if arg_wrnh == var_osiz(var_ayzf):
                var_ayzf.append(arg_rgwu.val)
            else:
                var_ayzf[arg_wrnh] = var_wnki(var_ayzf[arg_wrnh], arg_rgwu.val)
            func_hqta(arg_rgwu.left, arg_wrnh + 1)
            func_hqta(arg_rgwu.right, arg_wrnh + 1)
        var_ayzf = []
        func_hqta(arg_xdvx, 0)
        return var_ayzf
