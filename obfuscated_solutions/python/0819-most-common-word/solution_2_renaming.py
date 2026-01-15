class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_bacg:
        var_rgwu = var_wrnh(arg_rcsn)
        var_osiz = ''
        var_ayzf = 0
        var_wnki = var_egyk(var_dcmd)
        var_llti = []
        for var_zbxo, var_rdmc in var_rjut(arg_xdvx):
            if var_rdmc.isalnum():
                var_llti.append(var_rdmc.lower())
                if var_zbxo != var_lsgw(arg_xdvx) - 1:
                    continue
            if var_lsgw(var_llti) > 0:
                var_cbvh = ''.join(var_llti)
                if var_cbvh not in var_rgwu:
                    var_wnki[var_cbvh] += 1
                    if var_wnki[var_cbvh] > var_ayzf:
                        var_ayzf = var_wnki[var_cbvh]
                        var_osiz = var_cbvh
                var_llti = []
        return var_osiz
