class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_rgwu[var_hqta]) ->var_hqta:
        var_wrnh = var_osiz(var_ayzf)
        var_wnki = [0] * arg_xdvx
        for var_egyk, var_dcmd in arg_rcsn:
            var_wrnh[var_egyk - 1].append(var_dcmd - 1)
            var_wnki[var_dcmd - 1] += 1
        var_llti = var_zbxo()
        var_rdmc = [0] * arg_xdvx
        for var_rjut in var_lsgw(arg_xdvx):
            if var_wnki[var_rjut] == 0:
                var_llti.append(var_rjut)
                var_rdmc[var_rjut] = arg_bacg[var_rjut]
        while var_llti:
            var_rjut = var_llti.popleft()
            for var_cbvh in var_wrnh[var_rjut]:
                var_rdmc[var_cbvh] = var_yjch(var_rdmc[var_cbvh], var_rdmc[
                    var_rjut] + arg_bacg[var_cbvh])
                var_wnki[var_cbvh] -= 1
                if var_wnki[var_cbvh] == 0:
                    var_llti.append(var_cbvh)
        return var_yjch(var_rdmc)
