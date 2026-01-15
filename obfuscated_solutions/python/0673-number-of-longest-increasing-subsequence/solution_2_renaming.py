class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = [0] * var_rcsn
        var_rgwu = [0] * var_rcsn

        def func_wrnh(arg_osiz):
            if var_hqta[arg_osiz] != 0:
                return
            var_hqta[arg_osiz] = 1
            var_rgwu[arg_osiz] = 1
            for var_ayzf in var_wnki(arg_osiz):
                if arg_xdvx[var_ayzf] < arg_xdvx[arg_osiz]:
                    func_wrnh(var_ayzf)
                    if var_hqta[var_ayzf] + 1 > var_hqta[arg_osiz]:
                        var_hqta[arg_osiz] = var_hqta[var_ayzf] + 1
                        var_rgwu[arg_osiz] = 0
                    if var_hqta[var_ayzf] + 1 == var_hqta[arg_osiz]:
                        var_rgwu[arg_osiz] += var_rgwu[var_ayzf]
        var_egyk = 0
        var_dcmd = 0
        for arg_osiz in var_wnki(var_rcsn):
            func_wrnh(arg_osiz)
            var_egyk = var_llti(var_egyk, var_hqta[arg_osiz])
        for arg_osiz in var_wnki(var_rcsn):
            if var_hqta[arg_osiz] == var_egyk:
                var_dcmd += var_rgwu[arg_osiz]
        return var_dcmd
