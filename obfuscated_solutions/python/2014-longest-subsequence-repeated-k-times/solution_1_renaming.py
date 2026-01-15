class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_bacg:
        var_rgwu = ''
        var_wrnh = var_osiz([var_ayzf for var_ayzf, var_wnki in var_egyk(
            arg_xdvx).items() if var_wnki >= arg_rcsn], reverse=True)
        var_dcmd = var_llti(var_wrnh)
        while var_dcmd:
            var_zbxo = var_dcmd.popleft()
            if var_rdmc(var_zbxo) > var_rdmc(var_rgwu):
                var_rgwu = var_zbxo
            for var_rjut in var_wrnh:
                var_lsgw = var_zbxo + var_rjut
                var_cbvh = var_yjch(arg_xdvx)
                if var_dmio(var_rjut in var_cbvh for var_rjut in var_lsgw *
                    arg_rcsn):
                    var_dcmd.append(var_lsgw)
        return var_rgwu
