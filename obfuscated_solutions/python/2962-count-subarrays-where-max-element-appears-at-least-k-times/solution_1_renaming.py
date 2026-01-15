class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf = var_wnki = 0
        for var_egyk in var_dcmd(var_llti(arg_xdvx)):
            if arg_xdvx[var_egyk] == var_rgwu:
                var_wnki += 1
            while var_wnki == arg_rcsn:
                if arg_xdvx[var_ayzf] == var_rgwu:
                    var_wnki -= 1
                var_ayzf += 1
            var_osiz += var_ayzf
        return var_osiz
