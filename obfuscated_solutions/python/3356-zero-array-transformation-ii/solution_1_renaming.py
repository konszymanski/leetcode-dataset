class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz, var_ayzf = 0, var_wrnh(arg_rcsn)
        if not arg_ihhe.can_form_zero_array(arg_xdvx, arg_rcsn, var_ayzf):
            return -1
        while var_osiz <= var_ayzf:
            var_wnki = var_osiz + (var_ayzf - var_osiz) // 2
            if arg_ihhe.can_form_zero_array(arg_xdvx, arg_rcsn, var_wnki):
                var_ayzf = var_wnki - 1
            else:
                var_osiz = var_wnki + 1
        return var_osiz

    def func_egyk(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]], arg_dcmd: var_hqta) ->var_ulfl:
        var_rgwu = var_wrnh(arg_xdvx)
        var_llti = 0
        var_zbxo = [0] * (var_rgwu + 1)
        for var_rdmc in var_rjut(arg_dcmd):
            var_lsgw, var_cbvh, var_yjch = arg_rcsn[var_rdmc]
            var_zbxo[var_lsgw] += var_yjch
            var_zbxo[var_cbvh + 1] -= var_yjch
        for var_dmio in var_rjut(var_rgwu):
            var_llti += var_zbxo[var_dmio]
            if var_llti < arg_xdvx[var_dmio]:
                return False
        return True
