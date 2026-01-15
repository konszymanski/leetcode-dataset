class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = var_rgwu()
        for var_wrnh in var_osiz.product((0, 1), repeat=4):
            if var_ayzf(var_wrnh) % 2 == arg_rcsn % 2 and var_ayzf(var_wrnh
                ) <= arg_rcsn:
                var_wnki = []
                for var_egyk in var_dcmd(var_llti(arg_xdvx, 3)):
                    var_zbxo = 1
                    var_zbxo ^= var_wrnh[0]
                    var_zbxo ^= var_wrnh[1] and var_egyk % 2
                    var_zbxo ^= var_wrnh[2] and var_egyk % 2 == 0
                    var_zbxo ^= var_wrnh[3] and var_egyk % 3 == 0
                    var_wnki.append(var_zbxo)
                var_hqta.add(var_rdmc(var_wnki))
        return var_rjut(var_hqta)
