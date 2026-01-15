class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = []
        for var_hqta in var_rgwu(var_wrnh(arg_xdvx)):
            var_bacg.append([arg_xdvx[var_hqta][0], var_hqta])
            var_bacg.append([arg_xdvx[var_hqta][1], ~var_hqta])
        var_bacg.sort()
        var_osiz = var_ayzf(var_rgwu(var_wrnh(arg_xdvx)))
        var_wnki = []
        for var_egyk in var_bacg:
            var_dcmd, var_llti = var_egyk
            while var_wnki and var_wnki[0][0] <= var_dcmd:
                var_zbxo, var_rdmc = var_rjut.heappop(var_wnki)
                var_rjut.heappush(var_osiz, var_rdmc)
            if var_llti >= 0:
                var_rdmc = var_rjut.heappop(var_osiz)
                if var_llti == arg_rcsn:
                    return var_rdmc
                var_rjut.heappush(var_wnki, [arg_xdvx[var_llti][1], var_rdmc])
        return -1
