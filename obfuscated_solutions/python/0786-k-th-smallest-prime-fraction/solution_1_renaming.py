class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu, var_wrnh = 0, 1.0
        while var_rgwu < var_wrnh:
            var_osiz = (var_rgwu + var_wrnh) / 2
            var_ayzf = 0.0
            var_wnki = 0
            var_egyk, var_dcmd = 0, 0
            var_llti = 1
            for var_zbxo in var_rdmc(var_bacg - 1):
                while var_llti < var_bacg and arg_xdvx[var_zbxo
                    ] >= var_osiz * arg_xdvx[var_llti]:
                    var_llti += 1
                var_wnki += var_bacg - var_llti
                if var_llti == var_bacg:
                    break
                var_rjut = arg_xdvx[var_zbxo] / arg_xdvx[var_llti]
                if var_rjut > var_ayzf:
                    var_egyk = var_zbxo
                    var_dcmd = var_llti
                    var_ayzf = var_rjut
            if var_wnki == arg_rcsn:
                return [arg_xdvx[var_egyk], arg_xdvx[var_dcmd]]
            elif var_wnki > arg_rcsn:
                var_wrnh = var_osiz
            else:
                var_rgwu = var_osiz
        return []
