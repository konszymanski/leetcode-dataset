class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_bacg[var_hqta]]:

        def func_rgwu(arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta,
            arg_wrnh: var_hqta) ->var_bacg[var_bacg[var_hqta]]:
            var_osiz = []
            if not arg_xdvx:
                return var_osiz
            var_ayzf = arg_rcsn // arg_wrnh
            if var_ayzf < arg_xdvx[0] or arg_xdvx[-1] < var_ayzf:
                return var_osiz
            if arg_wrnh == 2:
                return var_wnki(arg_xdvx, arg_rcsn)
            for var_egyk in var_dcmd(var_llti(arg_xdvx)):
                if var_egyk == 0 or arg_xdvx[var_egyk - 1] != arg_xdvx[var_egyk
                    ]:
                    for var_zbxo in func_rgwu(arg_xdvx[var_egyk + 1:], 
                        arg_rcsn - arg_xdvx[var_egyk], arg_wrnh - 1):
                        var_osiz.append([arg_xdvx[var_egyk]] + var_zbxo)
            return var_osiz

        def var_wnki(arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
            ) ->var_bacg[var_bacg[var_hqta]]:
            var_osiz = []
            var_rdmc, var_rjut = 0, var_llti(arg_xdvx) - 1
            while var_rdmc < var_rjut:
                var_lsgw = arg_xdvx[var_rdmc] + arg_xdvx[var_rjut]
                if var_lsgw < arg_rcsn or var_rdmc > 0 and arg_xdvx[var_rdmc
                    ] == arg_xdvx[var_rdmc - 1]:
                    var_rdmc += 1
                elif var_lsgw > arg_rcsn or var_rjut < var_llti(arg_xdvx
                    ) - 1 and arg_xdvx[var_rjut] == arg_xdvx[var_rjut + 1]:
                    var_rjut -= 1
                else:
                    var_osiz.append([arg_xdvx[var_rdmc], arg_xdvx[var_rjut]])
                    var_rdmc += 1
                    var_rjut -= 1
            return var_osiz
        arg_xdvx.sort()
        return func_rgwu(arg_xdvx, arg_rcsn, 4)
