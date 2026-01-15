class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_hqta[var_rgwu]], arg_bacg: var_hqta[var_rgwu]) ->var_hqta[
        var_rgwu]:
        var_wrnh = var_osiz.fromkeys(arg_bacg, True)
        var_ayzf = {var_wnki: var_egyk for var_egyk, var_wnki in var_dcmd(
            arg_xdvx)}

        def func_llti(var_wnki: var_rgwu, arg_zbxo: var_rdmc) ->var_cbvh:
            if var_wrnh.get(var_wnki, False):
                return True
            if var_wnki not in var_ayzf or var_wnki in arg_zbxo:
                return False
            arg_zbxo.add(var_wnki)
            var_wrnh[var_wnki] = var_rjut(func_llti(var_lsgw, arg_zbxo) for
                var_lsgw in arg_rcsn[var_ayzf[var_wnki]])
            return var_wrnh[var_wnki]
        return [var_wnki for var_wnki in arg_xdvx if func_llti(var_wnki,
            var_rdmc())]
