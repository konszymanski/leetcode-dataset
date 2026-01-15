class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [0] * var_hqta
        var_osiz = [[] for var_ayzf in var_wnki(var_hqta)]
        for var_egyk in var_wnki(var_hqta):
            for var_dcmd in arg_xdvx[var_egyk]:
                var_osiz[var_dcmd].append(var_egyk)
                var_wrnh[var_egyk] += 1
        var_llti = var_zbxo()
        for var_egyk in var_wnki(var_hqta):
            if var_wrnh[var_egyk] == 0:
                var_llti.append(var_egyk)
        var_rdmc = [False] * var_hqta
        while var_llti:
            var_dcmd = var_llti.popleft()
            var_rdmc[var_dcmd] = True
            for var_rjut in var_osiz[var_dcmd]:
                var_wrnh[var_rjut] -= 1
                if var_wrnh[var_rjut] == 0:
                    var_llti.append(var_rjut)
        var_lsgw = []
        for var_egyk in var_wnki(var_hqta):
            if var_rdmc[var_egyk]:
                var_lsgw.append(var_egyk)
        return var_lsgw
