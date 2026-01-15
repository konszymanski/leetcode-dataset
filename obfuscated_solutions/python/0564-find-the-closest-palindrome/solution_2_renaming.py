class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_wrnh(var_bacg)
        var_osiz, var_ayzf = (var_rgwu - 1) // 2, var_rgwu // 2
        var_wnki = var_egyk(var_bacg)
        while var_osiz >= 0:
            var_wnki[var_ayzf] = var_wnki[var_osiz]
            var_ayzf += 1
            var_osiz -= 1
        return var_rcsn(''.join(var_wnki))

    def func_dcmd(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_llti, var_zbxo = 0, arg_xdvx
        var_rdmc = var_rjut('-inf')
        while var_llti <= var_zbxo:
            var_lsgw = (var_zbxo - var_llti) // 2 + var_llti
            var_cbvh = arg_ihhe.convert(var_lsgw)
            if var_cbvh < arg_xdvx:
                var_rdmc = var_cbvh
                var_llti = var_lsgw + 1
            else:
                var_zbxo = var_lsgw - 1
        return var_rdmc

    def func_yjch(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_llti, var_zbxo = arg_xdvx, var_rcsn(1e+18)
        var_rdmc = var_rjut('-inf')
        while var_llti <= var_zbxo:
            var_lsgw = (var_zbxo - var_llti) // 2 + var_llti
            var_cbvh = arg_ihhe.convert(var_lsgw)
            if var_cbvh > arg_xdvx:
                var_rdmc = var_cbvh
                var_zbxo = var_lsgw - 1
            else:
                var_llti = var_lsgw + 1
        return var_rdmc

    def func_dmio(arg_ihhe, var_rgwu: var_hqta) ->var_hqta:
        arg_xdvx = var_rcsn(var_rgwu)
        var_ulfl = arg_ihhe.previous_palindrome(arg_xdvx)
        var_lgvi = arg_ihhe.next_palindrome(arg_xdvx)
        if var_wvuc(var_ulfl - arg_xdvx) <= var_wvuc(var_lgvi - arg_xdvx):
            return var_hqta(var_ulfl)
        return var_hqta(var_lgvi)
