class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu.Counter(arg_bacg)
        var_wrnh = [(var_rgwu.Counter(var_osiz) & var_hqta) for var_osiz in
            arg_rcsn]
        for var_ayzf in var_wnki(var_egyk(var_wrnh) - 1, -1, -1):
            if var_dcmd(var_wrnh[var_ayzf] == var_wrnh[var_ayzf] & var_wrnh
                [var_llti] for var_llti in var_wnki(var_egyk(var_wrnh)) if 
                var_ayzf != var_llti):
                var_wrnh.pop(var_ayzf)
        arg_rcsn = [''.join(var_zbxo.elements()) for var_zbxo in var_wrnh]
        var_rdmc = [-1] * (1 << var_egyk(arg_bacg))
        var_rdmc[0] = 0
        for var_rjut in var_lsgw(1 << var_egyk(arg_bacg)):
            if var_rdmc[var_rjut] == -1:
                continue
            for var_osiz in arg_rcsn:
                var_cbvh = var_rjut
                for var_yjch in var_osiz:
                    for var_ayzf, var_dmio in var_ulfl(arg_bacg):
                        if var_cbvh >> var_ayzf & 1:
                            continue
                        if var_dmio == var_yjch:
                            var_cbvh |= 1 << var_ayzf
                            break
                if var_rdmc[var_cbvh] == -1 or var_rdmc[var_cbvh] > var_rdmc[
                    var_rjut] + 1:
                    var_rdmc[var_cbvh] = var_rdmc[var_rjut] + 1
        return var_rdmc[-1]
