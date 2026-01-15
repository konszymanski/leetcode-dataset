class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])

        def func_osiz():
            var_ayzf = var_wnki()
            var_egyk = 0
            for var_dcmd in var_llti(var_hqta):
                for var_zbxo in var_llti(var_rgwu):
                    if arg_xdvx[var_dcmd][var_zbxo] == 1 and (var_dcmd,
                        var_zbxo) not in var_ayzf:
                        var_rdmc(var_dcmd, var_zbxo, var_ayzf)
                        var_egyk += 1
            return var_egyk

        def var_rdmc(var_dcmd, var_zbxo, var_ayzf):
            if (var_dcmd < 0 or var_dcmd >= var_hqta or var_zbxo < 0 or 
                var_zbxo >= var_rgwu or arg_xdvx[var_dcmd][var_zbxo] == 0 or
                (var_dcmd, var_zbxo) in var_ayzf):
                return
            var_ayzf.add((var_dcmd, var_zbxo))
            for var_rjut, var_lsgw in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                var_rdmc(var_dcmd + var_rjut, var_zbxo + var_lsgw, var_ayzf)
        if func_osiz() != 1:
            return 0
        for var_dcmd in var_llti(var_hqta):
            for var_zbxo in var_llti(var_rgwu):
                if arg_xdvx[var_dcmd][var_zbxo] == 1:
                    arg_xdvx[var_dcmd][var_zbxo] = 0
                    if func_osiz() != 1:
                        return 1
                    arg_xdvx[var_dcmd][var_zbxo] = 1
        return 2
