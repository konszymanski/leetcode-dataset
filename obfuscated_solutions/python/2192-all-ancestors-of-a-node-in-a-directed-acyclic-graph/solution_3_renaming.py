class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = [[] for var_hqta in var_rgwu(arg_xdvx)]
        var_wrnh = [(0) for var_hqta in var_rgwu(arg_xdvx)]
        for var_osiz, var_ayzf in arg_rcsn:
            var_bacg[var_osiz].append(var_ayzf)
            var_wrnh[var_ayzf] += 1
        var_wnki = [var_egyk for var_egyk in var_rgwu(arg_xdvx) if var_wrnh
            [var_egyk] == 0]
        var_dcmd = []
        while var_wnki:
            var_llti = var_wnki.pop(0)
            var_dcmd.append(var_llti)
            for var_zbxo in var_bacg[var_llti]:
                var_wrnh[var_zbxo] -= 1
                if var_wrnh[var_zbxo] == 0:
                    var_wnki.append(var_zbxo)
        var_rdmc = [[] for var_hqta in var_rgwu(arg_xdvx)]
        var_rjut = [var_lsgw() for var_hqta in var_rgwu(arg_xdvx)]
        for var_cbvh in var_dcmd:
            for var_zbxo in var_bacg[var_cbvh]:
                var_rjut[var_zbxo].add(var_cbvh)
                var_rjut[var_zbxo].update(var_rjut[var_cbvh])
        for var_egyk in var_rgwu(arg_xdvx):
            for var_cbvh in var_rgwu(arg_xdvx):
                if var_cbvh == var_egyk:
                    continue
                if var_cbvh in var_rjut[var_egyk]:
                    var_rdmc[var_egyk].append(var_cbvh)
        return var_rdmc
