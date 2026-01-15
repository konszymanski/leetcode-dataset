class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_wrnh,
        arg_bacg: var_wrnh, arg_hqta: var_rgwu) ->var_rgwu:
        var_osiz = []
        var_ayzf = 0
        var_wnki = arg_xdvx
        while var_ayzf < arg_rcsn:
            var_osiz.append(var_wnki.val)
            var_wnki = var_wnki.next
            var_ayzf += 1
        var_egyk = arg_hqta
        while var_egyk is not None:
            var_osiz.append(var_egyk.val)
            var_egyk = var_egyk.next
        while var_ayzf < arg_bacg + 1:
            var_wnki = var_wnki.next
            var_ayzf += 1
        while var_wnki is not None:
            var_osiz.append(var_wnki.val)
            var_wnki = var_wnki.next
        var_dcmd = None
        for var_llti in var_zbxo(var_rdmc(var_osiz)):
            var_rjut = var_rgwu(var_osiz.pop(), var_dcmd)
            var_dcmd = var_rjut
        return var_dcmd
