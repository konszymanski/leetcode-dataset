class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):

        def func_hqta(arg_rgwu):
            return var_wrnh(arg_rcsn[(var_osiz + arg_rgwu) % var_ayzf(
                arg_rcsn)] == var_wnki for var_osiz, var_wnki in var_egyk(
                arg_bacg))
        var_dcmd = (var_ayzf(arg_bacg) - 1) // var_ayzf(arg_rcsn) + 1
        var_llti, var_zbxo = 113, 10 ** 9 + 7
        var_rdmc = var_rjut(var_llti, var_zbxo - 2, var_zbxo)
        var_lsgw = 1
        var_cbvh = 0
        for var_wnki in var_yjch(var_dmio, arg_bacg):
            var_cbvh += var_lsgw * var_wnki
            var_cbvh %= var_zbxo
            var_lsgw = var_lsgw * var_llti % var_zbxo
        var_ulfl = 0
        var_lsgw = 1
        for var_osiz in var_lgvi(var_ayzf(arg_bacg)):
            var_ulfl += var_lsgw * var_dmio(arg_rcsn[var_osiz % var_ayzf(
                arg_rcsn)])
            var_ulfl %= var_zbxo
            var_lsgw = var_lsgw * var_llti % var_zbxo
        if var_ulfl == var_cbvh and func_hqta(0):
            return var_dcmd
        var_lsgw = var_lsgw * var_rdmc % var_zbxo
        for var_osiz in var_lgvi(var_ayzf(arg_bacg), (var_dcmd + 1) *
            var_ayzf(arg_rcsn)):
            var_ulfl = (var_ulfl - var_dmio(arg_rcsn[(var_osiz - var_ayzf(
                arg_bacg)) % var_ayzf(arg_rcsn)])) * var_rdmc
            var_ulfl += var_lsgw * var_dmio(arg_rcsn[var_osiz % var_ayzf(
                arg_rcsn)])
            var_ulfl %= var_zbxo
            if var_ulfl == var_cbvh and func_hqta(var_osiz - var_ayzf(
                arg_bacg) + 1):
                return var_dcmd if var_osiz < var_dcmd * var_ayzf(arg_rcsn
                    ) else var_dcmd + 1
        return -1
