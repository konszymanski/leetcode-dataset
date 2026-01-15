class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = []
        var_rgwu = var_wrnh(arg_bacg) % 26
        for var_osiz, var_ayzf in var_wnki(arg_rcsn):
            var_egyk = var_dcmd(var_ayzf) - var_dcmd('a')
            var_hqta.append(var_llti(var_dcmd('a') + (var_egyk + var_rgwu) %
                26))
            var_rgwu = (var_rgwu - arg_bacg[var_osiz]) % 26
        return ''.join(var_hqta)
