class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = 0
        var_wrnh = {}
        var_wrnh[var_bacg[0]] = var_rgwu
        var_osiz = {}
        var_osiz[var_rgwu] = var_ayzf([var_bacg[0]])
        for var_wnki in var_egyk(1, var_dcmd(arg_xdvx)):
            if var_llti(var_bacg[var_wnki] - var_bacg[var_wnki - 1]
                ) > arg_rcsn:
                var_rgwu += 1
            var_wrnh[var_bacg[var_wnki]] = var_rgwu
            if var_rgwu not in var_osiz:
                var_osiz[var_rgwu] = var_ayzf()
            var_osiz[var_rgwu].append(var_bacg[var_wnki])
        for var_wnki in var_egyk(var_dcmd(arg_xdvx)):
            var_zbxo = arg_xdvx[var_wnki]
            var_rdmc = var_wrnh[var_zbxo]
            arg_xdvx[var_wnki] = var_osiz[var_rdmc].popleft()
        return arg_xdvx
