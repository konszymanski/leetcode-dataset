class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_dcmd:
        var_rgwu = var_wrnh([1] + arg_xdvx + [arg_rcsn])
        return {(var_rgwu[var_osiz] - var_rgwu[var_ayzf]) for var_ayzf in
            var_wnki(var_egyk(var_rgwu)) for var_osiz in var_wnki(var_ayzf +
            1, var_egyk(var_rgwu))}

    def func_llti(arg_ihhe, arg_zbxo: var_hqta, arg_rdmc: var_hqta,
        arg_rjut: var_bacg[var_hqta], arg_lsgw: var_bacg[var_hqta]) ->var_hqta:
        var_cbvh = 10 ** 9 + 7
        var_yjch = arg_ihhe.get_edges(arg_rjut, arg_zbxo)
        var_dmio = arg_ihhe.get_edges(arg_lsgw, arg_rdmc)
        var_ulfl = var_lgvi(var_yjch & var_dmio, default=0)
        return var_ulfl * var_ulfl % var_cbvh if var_ulfl else -1
