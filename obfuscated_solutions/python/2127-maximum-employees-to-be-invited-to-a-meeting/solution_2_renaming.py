class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [0] * var_hqta
        for var_osiz in var_ayzf(var_hqta):
            var_wrnh[arg_xdvx[var_osiz]] += 1
        var_wnki = var_egyk()
        for var_osiz in var_ayzf(var_hqta):
            if var_wrnh[var_osiz] == 0:
                var_wnki.append(var_osiz)
        var_dcmd = [1] * var_hqta
        while var_wnki:
            var_llti = var_wnki.popleft()
            var_zbxo = arg_xdvx[var_llti]
            var_dcmd[var_zbxo] = var_rdmc(var_dcmd[var_zbxo], var_dcmd[
                var_llti] + 1)
            var_wrnh[var_zbxo] -= 1
            if var_wrnh[var_zbxo] == 0:
                var_wnki.append(var_zbxo)
        var_rjut = 0
        var_lsgw = 0
        for var_osiz in var_ayzf(var_hqta):
            if var_wrnh[var_osiz] == 0:
                continue
            var_cbvh = 0
            var_yjch = var_osiz
            while var_wrnh[var_yjch] != 0:
                var_wrnh[var_yjch] = 0
                var_cbvh += 1
                var_yjch = arg_xdvx[var_yjch]
            if var_cbvh == 2:
                var_lsgw += var_dcmd[var_osiz] + var_dcmd[arg_xdvx[var_osiz]]
            else:
                var_rjut = var_rdmc(var_rjut, var_cbvh)
        return var_rdmc(var_rjut, var_lsgw)
