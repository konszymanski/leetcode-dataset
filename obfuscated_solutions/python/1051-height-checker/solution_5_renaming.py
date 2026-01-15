class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = [[] for var_hqta in var_rgwu(10)]
        for var_wrnh in arg_xdvx:
            var_osiz = var_ayzf(var_wrnh) // arg_rcsn
            var_osiz = var_osiz % 10
            var_bacg[var_osiz].append(var_wrnh)
        var_wnki = 0
        for var_osiz in var_rgwu(10):
            for var_wrnh in var_bacg[var_osiz]:
                arg_xdvx[var_wnki] = var_wrnh
                var_wnki += 1

    def func_egyk(arg_ihhe, arg_xdvx):
        var_dcmd, var_llti = var_zbxo(var_ayzf(var_wrnh) for var_wrnh in
            arg_xdvx), 0
        while var_dcmd > 0:
            var_llti += 1
            var_dcmd //= 10
        arg_rcsn = 1
        for var_hqta in var_rgwu(var_llti):
            arg_ihhe.bucket_sort(arg_xdvx, arg_rcsn)
            arg_rcsn *= 10

    def func_rdmc(arg_ihhe, arg_rjut: var_lsgw[var_cbvh]) ->var_cbvh:
        var_yjch = arg_rjut[:]
        arg_ihhe.radix_sort(var_yjch)
        var_dmio = 0
        for var_ulfl in var_rgwu(var_lgvi(var_yjch)):
            if arg_rjut[var_ulfl] != var_yjch[var_ulfl]:
                var_dmio += 1
        return var_dmio
