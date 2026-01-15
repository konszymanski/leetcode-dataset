class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_rcsn)
        var_wrnh = var_rgwu(arg_bacg)
        var_osiz = {var_ayzf: [] for var_ayzf in arg_bacg}
        var_wnki = []
        var_egyk = 0
        for var_dcmd in var_hqta:
            if var_dcmd > var_wrnh[var_egyk]:
                var_osiz[var_wrnh[var_egyk]].append(var_dcmd)
                var_egyk += 1
            else:
                var_wnki.append(var_dcmd)
        return [(var_osiz[var_ayzf].pop() if var_osiz[var_ayzf] else
            var_wnki.pop()) for var_ayzf in arg_bacg]
