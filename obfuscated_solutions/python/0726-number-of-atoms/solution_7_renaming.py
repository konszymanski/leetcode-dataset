class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta.findall('([A-Z][a-z]*)(\\d*)|(\\()|(\\))(\\d*)',
            arg_xdvx)
        var_bacg.reverse()
        var_rgwu = var_wrnh(var_osiz)
        var_ayzf = [1]
        var_wnki = 1
        for var_egyk, var_dcmd, var_llti, var_zbxo, var_rdmc in var_bacg:
            if var_egyk:
                if var_dcmd:
                    var_rgwu[var_egyk] += var_osiz(var_dcmd) * var_wnki
                else:
                    var_rgwu[var_egyk] += 1 * var_wnki
            elif var_zbxo:
                if not var_rdmc:
                    var_rdmc = 1
                else:
                    var_rdmc = var_osiz(var_rdmc)
                var_wnki *= var_rdmc
                var_ayzf.append(var_rdmc)
            elif var_llti:
                var_wnki //= var_ayzf.pop()
        var_rgwu = var_rjut(var_lsgw(var_rgwu.items()))
        var_cbvh = ''
        for var_egyk in var_rgwu:
            var_cbvh += var_egyk
            if var_rgwu[var_egyk] > 1:
                var_cbvh += var_rcsn(var_rgwu[var_egyk])
        return var_cbvh
