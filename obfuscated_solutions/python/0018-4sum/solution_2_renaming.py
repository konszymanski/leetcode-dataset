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
            var_rdmc = var_rjut()
            for var_egyk in var_dcmd(var_llti(arg_xdvx)):
                if var_llti(var_osiz) == 0 or var_osiz[-1][1] != arg_xdvx[
                    var_egyk]:
                    if arg_rcsn - arg_xdvx[var_egyk] in var_rdmc:
                        var_osiz.append([arg_rcsn - arg_xdvx[var_egyk],
                            arg_xdvx[var_egyk]])
                var_rdmc.add(arg_xdvx[var_egyk])
            return var_osiz
        arg_xdvx.sort()
        return func_rgwu(arg_xdvx, arg_rcsn, 4)
