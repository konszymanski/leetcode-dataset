class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta, arg_rgwu):
        if arg_xdvx == var_wrnh(arg_bacg):
            return arg_rcsn == arg_hqta
        if arg_rcsn > arg_hqta:
            return False
        if arg_rgwu[arg_xdvx][arg_rcsn] != -1:
            return arg_rgwu[arg_xdvx][arg_rcsn] == 1
        var_osiz = False
        for var_ayzf in var_wnki(arg_xdvx, var_wrnh(arg_bacg)):
            var_egyk = arg_bacg[arg_xdvx:var_ayzf + 1]
            var_dcmd = var_llti(var_egyk)
            var_osiz = var_osiz or arg_ihhe.find_partitions(var_ayzf + 1, 
                arg_rcsn + var_dcmd, arg_bacg, arg_hqta, arg_rgwu)
            if var_osiz:
                arg_rgwu[arg_xdvx][arg_rcsn] = 1
                return True
        arg_rgwu[arg_xdvx][arg_rcsn] = 0
        return False

    def func_zbxo(arg_ihhe, arg_rdmc: var_llti) ->var_llti:
        var_rjut = 0
        for var_lsgw in var_wnki(1, arg_rdmc + 1):
            var_cbvh = var_lsgw * var_lsgw
            arg_bacg = var_yjch(var_cbvh)
            var_dmio = [([-1] * (var_lsgw + 1)) for var_ulfl in var_wnki(
                var_wrnh(arg_bacg))]
            if arg_ihhe.find_partitions(0, 0, arg_bacg, var_lsgw, var_dmio):
                var_rjut += var_cbvh
        return var_rjut
