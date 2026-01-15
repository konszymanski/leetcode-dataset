class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh('inf')
        var_osiz = var_ayzf = 0
        var_wnki = [0] * 32
        while var_ayzf < var_egyk(arg_xdvx):
            arg_ihhe._update_bit_counts(var_wnki, arg_xdvx[var_ayzf], 1)
            while var_osiz <= var_ayzf and arg_ihhe._convert_bits_to_num(
                var_wnki) >= arg_rcsn:
                var_rgwu = var_dcmd(var_rgwu, var_ayzf - var_osiz + 1)
                arg_ihhe._update_bit_counts(var_wnki, arg_xdvx[var_osiz], -1)
                var_osiz += 1
            var_ayzf += 1
        return -1 if var_rgwu == var_wrnh('inf') else var_rgwu

    def func_llti(arg_ihhe, var_wnki: var_rjut, arg_zbxo: var_hqta,
        arg_rdmc: var_hqta) ->None:
        for var_lsgw in var_cbvh(32):
            if arg_zbxo & 1 << var_lsgw:
                var_wnki[var_lsgw] += arg_rdmc

    def func_yjch(arg_ihhe, var_wnki: var_rjut) ->var_hqta:
        var_dmio = 0
        for var_lsgw in var_cbvh(32):
            if var_wnki[var_lsgw]:
                var_dmio |= 1 << var_lsgw
        return var_dmio
