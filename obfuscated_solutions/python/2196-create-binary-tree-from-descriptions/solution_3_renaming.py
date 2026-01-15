class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rdmc[
        var_llti]:
        var_hqta = {}
        var_rgwu = var_wrnh()
        for var_osiz in arg_xdvx:
            var_ayzf = var_osiz[0]
            var_wnki = var_osiz[1]
            var_egyk = var_dcmd(var_osiz[2])
            if var_ayzf not in var_hqta:
                var_hqta[var_ayzf] = var_llti(var_ayzf)
            if var_wnki not in var_hqta:
                var_hqta[var_wnki] = var_llti(var_wnki)
            if var_egyk:
                var_hqta[var_ayzf].left = var_hqta[var_wnki]
            else:
                var_hqta[var_ayzf].right = var_hqta[var_wnki]
            var_rgwu.add(var_wnki)
        for var_zbxo in var_hqta.values():
            if var_zbxo.val not in var_rgwu:
                return var_zbxo
        return None
