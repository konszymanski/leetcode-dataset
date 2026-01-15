class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_zbxo:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = 0
        for var_wrnh in var_bacg:
            var_osiz, var_ayzf = arg_xdvx.index(var_wrnh), arg_xdvx.rindex(
                var_wrnh)
            var_wnki = var_hqta()
            for var_egyk in var_dcmd(var_osiz + 1, var_ayzf):
                var_wnki.add(arg_xdvx[var_egyk])
            var_rgwu += var_llti(var_wnki)
        return var_rgwu
