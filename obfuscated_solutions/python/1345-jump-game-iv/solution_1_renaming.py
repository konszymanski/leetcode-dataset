class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        if var_hqta <= 1:
            return 0
        var_wrnh = {}
        for var_osiz in var_ayzf(var_hqta):
            if arg_xdvx[var_osiz] in var_wrnh:
                var_wrnh[arg_xdvx[var_osiz]].append(var_osiz)
            else:
                var_wrnh[arg_xdvx[var_osiz]] = [var_osiz]
        var_wnki = [0]
        var_egyk = {0}
        var_dcmd = 0
        while var_wnki:
            var_llti = []
            for var_zbxo in var_wnki:
                if var_zbxo == var_hqta - 1:
                    return var_dcmd
                for var_rdmc in var_wrnh[arg_xdvx[var_zbxo]]:
                    if var_rdmc not in var_egyk:
                        var_egyk.add(var_rdmc)
                        var_llti.append(var_rdmc)
                var_wrnh[arg_xdvx[var_zbxo]].clear()
                for var_rdmc in [var_zbxo - 1, var_zbxo + 1]:
                    if 0 <= var_rdmc < var_rgwu(arg_xdvx
                        ) and var_rdmc not in var_egyk:
                        var_egyk.add(var_rdmc)
                        var_llti.append(var_rdmc)
            var_wnki = var_llti
            var_dcmd += 1
        return -1
