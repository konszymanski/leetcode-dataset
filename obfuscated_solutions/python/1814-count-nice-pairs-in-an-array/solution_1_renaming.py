class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:

        def func_hqta(arg_rgwu):
            var_wrnh = 0
            while arg_rgwu:
                var_wrnh = var_wrnh * 10 + arg_rgwu % 10
                arg_rgwu //= 10
            return var_wrnh
        var_osiz = []
        for var_ayzf in var_wnki(var_egyk(arg_xdvx)):
            var_osiz.append(arg_xdvx[var_ayzf] - func_hqta(arg_xdvx[var_ayzf]))
        var_dcmd = var_llti(var_bacg)
        var_zbxo = 0
        var_rdmc = 10 ** 9 + 7
        for arg_rgwu in var_osiz:
            var_zbxo = (var_zbxo + var_dcmd[arg_rgwu]) % var_rdmc
            var_dcmd[arg_rgwu] += 1
        return var_zbxo
