class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = []
        arg_ihhe.permute(var_rcsn, arg_xdvx, 0)
        return var_rcsn

    def func_bacg(arg_ihhe, var_rcsn, arg_xdvx, arg_hqta):
        if arg_hqta >= var_rgwu(arg_xdvx):
            var_rcsn.append(arg_xdvx[:])
        else:
            for var_wrnh in var_osiz(arg_hqta, var_rgwu(arg_xdvx)):
                arg_xdvx[arg_hqta], arg_xdvx[var_wrnh] = arg_xdvx[var_wrnh
                    ], arg_xdvx[arg_hqta]
                arg_ihhe.permute(var_rcsn, arg_xdvx, arg_hqta + 1)
                arg_xdvx[arg_hqta], arg_xdvx[var_wrnh] = arg_xdvx[var_wrnh
                    ], arg_xdvx[arg_hqta]

    def func_ayzf(arg_ihhe, arg_wnki):
        var_egyk = [False] * var_rgwu(arg_wnki)
        var_rcsn = 0
        for var_wrnh in var_osiz(var_rgwu(arg_wnki) - 1):
            var_dcmd = var_llti(arg_wnki[var_wrnh] - arg_wnki[var_wrnh + 1])
            if not var_egyk[var_dcmd]:
                var_rcsn += 1
                var_egyk[var_dcmd] = True
        return var_rcsn

    def func_zbxo(arg_ihhe, arg_rdmc, arg_rjut):
        arg_xdvx = [(var_wrnh + 1) for var_wrnh in var_osiz(arg_rdmc)]
        for var_lsgw in arg_ihhe.permutations(arg_xdvx):
            if arg_ihhe.numUniqueDiffs(var_lsgw) == arg_rjut:
                return var_lsgw
        return []
