class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = 0
        var_wrnh = 1
        var_osiz = arg_xdvx[0]
        for var_ayzf in var_wnki(1, var_bacg):
            if arg_xdvx[var_ayzf] == var_osiz:
                var_wrnh = 1
                var_osiz = arg_xdvx[var_ayzf]
                continue
            var_wrnh += 1
            if var_wrnh >= arg_rcsn:
                var_rgwu += 1
            var_osiz = arg_xdvx[var_ayzf]
        for var_ayzf in var_wnki(arg_rcsn - 1):
            if arg_xdvx[var_ayzf] == var_osiz:
                break
            var_wrnh += 1
            if var_wrnh >= arg_rcsn:
                var_rgwu += 1
            var_osiz = arg_xdvx[var_ayzf]
        return var_rgwu
