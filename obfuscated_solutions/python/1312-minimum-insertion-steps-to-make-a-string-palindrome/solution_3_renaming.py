class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        var_rgwu = [0] * (arg_hqta + 1)
        var_wrnh = [0] * (arg_hqta + 1)
        for var_osiz in var_ayzf(arg_bacg + 1):
            for var_wnki in var_ayzf(arg_hqta + 1):
                if var_osiz == 0 or var_wnki == 0:
                    var_rgwu[var_wnki] = 0
                elif arg_xdvx[var_osiz - 1] == arg_rcsn[var_wnki - 1]:
                    var_rgwu[var_wnki] = 1 + var_wrnh[var_wnki - 1]
                else:
                    var_rgwu[var_wnki] = var_egyk(var_wrnh[var_wnki],
                        var_rgwu[var_wnki - 1])
            var_wrnh = var_dcmd(var_rgwu)
        return var_rgwu[arg_hqta]

    def func_llti(arg_ihhe, arg_zbxo):
        arg_hqta = var_rdmc(arg_zbxo)
        var_rjut = arg_zbxo[::-1]
        return arg_hqta - arg_ihhe.lcs(arg_zbxo, var_rjut, arg_hqta, arg_hqta)
