class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = {var_rgwu(var_wrnh) for var_wrnh in arg_bacg}
        var_osiz = [([0] * arg_rcsn) for var_ayzf in var_wnki(arg_rcsn)]
        var_egyk = 0
        for var_dcmd in var_wnki(arg_rcsn):
            var_llti = 0
            for var_zbxo in var_wnki(arg_rcsn):
                var_llti = 0 if (var_dcmd, var_zbxo
                    ) in var_hqta else var_llti + 1
                var_osiz[var_dcmd][var_zbxo] = var_llti
            var_llti = 0
            for var_zbxo in var_wnki(arg_rcsn - 1, -1, -1):
                var_llti = 0 if (var_dcmd, var_zbxo
                    ) in var_hqta else var_llti + 1
                if var_llti < var_osiz[var_dcmd][var_zbxo]:
                    var_osiz[var_dcmd][var_zbxo] = var_llti
        for var_zbxo in var_wnki(arg_rcsn):
            var_llti = 0
            for var_dcmd in var_wnki(arg_rcsn):
                var_llti = 0 if (var_dcmd, var_zbxo
                    ) in var_hqta else var_llti + 1
                if var_llti < var_osiz[var_dcmd][var_zbxo]:
                    var_osiz[var_dcmd][var_zbxo] = var_llti
            var_llti = 0
            for var_dcmd in var_wnki(arg_rcsn - 1, -1, -1):
                var_llti = 0 if (var_dcmd, var_zbxo
                    ) in var_hqta else var_llti + 1
                if var_llti < var_osiz[var_dcmd][var_zbxo]:
                    var_osiz[var_dcmd][var_zbxo] = var_llti
                if var_osiz[var_dcmd][var_zbxo] > var_egyk:
                    var_egyk = var_osiz[var_dcmd][var_zbxo]
        return var_egyk
