class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rjut:
        var_bacg = [([0] * (var_hqta(arg_xdvx) + 1)) for var_rgwu in
            var_wrnh(26)]
        var_osiz = arg_xdvx[0]
        var_ayzf = 1
        var_bacg[var_wnki(arg_xdvx[0]) - var_wnki('a')][1] = 1
        var_egyk = -1
        for var_dcmd in var_wrnh(1, var_hqta(arg_xdvx)):
            var_llti = arg_xdvx[var_dcmd]
            if var_llti == var_osiz:
                var_ayzf += 1
                var_bacg[var_wnki(var_llti) - var_wnki('a')][var_ayzf] += 1
            else:
                var_osiz = var_llti
                var_ayzf = 1
                var_bacg[var_wnki(var_llti) - var_wnki('a')][1] += 1
        for var_dcmd in var_wrnh(26):
            for var_zbxo in var_wrnh(var_hqta(arg_xdvx) - 1, 0, -1):
                var_bacg[var_dcmd][var_zbxo] += var_bacg[var_dcmd][var_zbxo + 1
                    ]
                if var_bacg[var_dcmd][var_zbxo] >= 3:
                    var_egyk = var_rdmc(var_egyk, var_zbxo)
                    break
        return var_egyk
