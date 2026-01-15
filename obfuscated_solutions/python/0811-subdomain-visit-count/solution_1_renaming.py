class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta.Counter()
        for var_rgwu in arg_rcsn:
            var_wrnh, var_rgwu = var_rgwu.split()
            var_wrnh = var_osiz(var_wrnh)
            var_ayzf = var_rgwu.split('.')
            for var_wnki in var_egyk(var_dcmd(var_ayzf)):
                var_bacg['.'.join(var_ayzf[var_wnki:])] += var_wrnh
        return ['{} {}'.format(var_llti, var_zbxo) for var_zbxo, var_llti in
            var_bacg.items()]
