class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_hqta[var_rgwu]:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = var_wnki()
        for var_egyk in var_dcmd(var_wrnh - arg_rcsn + 1):
            var_llti = var_zbxo(arg_xdvx[var_egyk:var_egyk + arg_rcsn])
            var_rdmc = var_rjut(var_llti.items(), key=lambda item: (-
                var_lsgw[1], -var_lsgw[0]))
            var_cbvh = var_yjch(var_dmio * var_ulfl for var_dmio, var_ulfl in
                var_rdmc[:arg_bacg])
            var_ayzf.append(var_cbvh)
        return var_ayzf
