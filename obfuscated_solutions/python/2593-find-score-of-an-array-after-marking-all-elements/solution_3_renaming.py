class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = 0
        while var_rgwu < var_wrnh(arg_xdvx):
            var_osiz = var_rgwu
            while var_rgwu + 1 < var_wrnh(arg_xdvx) and arg_xdvx[var_rgwu + 1
                ] < arg_xdvx[var_rgwu]:
                var_rgwu += 1
            var_ayzf = var_rgwu
            while var_ayzf >= var_osiz:
                var_hqta += arg_xdvx[var_ayzf]
                var_ayzf -= 2
            var_rgwu += 2
        return var_hqta
