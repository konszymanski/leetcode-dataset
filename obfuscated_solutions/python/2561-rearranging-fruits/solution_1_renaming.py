class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = var_wrnh()
        var_osiz = var_ayzf('inf')
        for var_wnki in arg_xdvx:
            var_rgwu[var_wnki] += 1
            var_osiz = var_egyk(var_osiz, var_wnki)
        for var_dcmd in arg_rcsn:
            var_rgwu[var_dcmd] -= 1
            var_osiz = var_egyk(var_osiz, var_dcmd)
        var_llti = []
        for var_zbxo, var_rdmc in var_rgwu.items():
            if var_rdmc % 2 != 0:
                return -1
            var_llti.extend([var_zbxo] * (var_rjut(var_rdmc) // 2))
        if not var_llti:
            return 0
        var_llti.sort()
        return var_lsgw(var_egyk(2 * var_osiz, var_cbvh) for var_cbvh in
            var_llti[:var_yjch(var_llti) // 2])
