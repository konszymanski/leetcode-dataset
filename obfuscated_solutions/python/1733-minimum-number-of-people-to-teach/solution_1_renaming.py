class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_rgwu[var_rgwu[var_hqta]]) ->var_hqta:
        var_wrnh = var_osiz()
        for var_ayzf in arg_bacg:
            var_wnki = {}
            var_egyk = False
            for var_dcmd in arg_rcsn[var_ayzf[0] - 1]:
                var_wnki[var_dcmd] = 1
            for var_dcmd in arg_rcsn[var_ayzf[1] - 1]:
                if var_dcmd in var_wnki:
                    var_egyk = True
                    break
            if not var_egyk:
                var_wrnh.add(var_ayzf[0] - 1)
                var_wrnh.add(var_ayzf[1] - 1)
        var_llti = 0
        var_zbxo = [0] * (arg_xdvx + 1)
        for var_ayzf in var_wrnh:
            for var_dcmd in arg_rcsn[var_ayzf]:
                var_zbxo[var_dcmd] += 1
                var_llti = var_rdmc(var_llti, var_zbxo[var_dcmd])
        return var_rjut(var_wrnh) - var_llti
