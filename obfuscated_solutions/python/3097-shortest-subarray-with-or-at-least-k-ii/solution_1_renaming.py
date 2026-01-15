class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu, var_wrnh = 1, var_osiz(arg_xdvx)
        var_ayzf = -1
        while var_rgwu <= var_wrnh:
            var_wnki = var_rgwu + (var_wrnh - var_rgwu) // 2
            if arg_ihhe._has_valid_subarray(arg_xdvx, arg_rcsn, var_wnki):
                var_ayzf = var_wnki
                var_wrnh = var_wnki - 1
            else:
                var_rgwu = var_wnki + 1
        return var_ayzf

    def func_egyk(arg_ihhe, arg_xdvx: var_zbxo, arg_dcmd: var_hqta,
        arg_llti: var_hqta) ->var_lsgw:
        var_rdmc = [0] * 32
        for var_wrnh in var_rjut(var_osiz(arg_xdvx)):
            arg_ihhe._update_bit_counts(var_rdmc, arg_xdvx[var_wrnh], 1)
            if var_wrnh >= arg_llti:
                arg_ihhe._update_bit_counts(var_rdmc, arg_xdvx[var_wrnh -
                    arg_llti], -1)
            if var_wrnh >= arg_llti - 1 and arg_ihhe._convert_bits_to_num(
                var_rdmc) >= arg_dcmd:
                return True
        return False

    def func_cbvh(arg_ihhe, var_rdmc: var_zbxo, arg_yjch: var_hqta,
        arg_dmio: var_hqta) ->None:
        for var_ulfl in var_rjut(32):
            if arg_yjch & 1 << var_ulfl:
                var_rdmc[var_ulfl] += arg_dmio

    def func_lgvi(arg_ihhe, var_rdmc: var_zbxo) ->var_hqta:
        return var_wvuc(1 << var_ulfl for var_ulfl in var_rjut(32) if
            var_rdmc[var_ulfl])
