class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        if arg_xdvx == '0' or arg_rcsn == '0':
            return '0'
        var_hqta = var_rgwu(arg_xdvx) + var_rgwu(arg_rcsn)
        var_wrnh = [0] * var_hqta
        var_osiz = arg_xdvx[::-1]
        var_ayzf = arg_rcsn[::-1]
        for var_wnki, var_egyk in var_dcmd(var_ayzf):
            for var_llti, var_zbxo in var_dcmd(var_osiz):
                var_rdmc = var_llti + var_wnki
                var_rjut = var_wrnh[var_rdmc]
                var_lsgw = var_cbvh(var_zbxo) * var_cbvh(var_egyk) + var_rjut
                var_wrnh[var_rdmc] = var_lsgw % 10
                var_wrnh[var_rdmc + 1] += var_lsgw // 10
        if var_wrnh[-1] == 0:
            var_wrnh.pop()
        return ''.join(var_bacg(var_yjch) for var_yjch in var_dmio(var_wrnh))
