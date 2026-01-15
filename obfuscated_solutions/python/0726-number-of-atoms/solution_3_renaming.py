class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = [var_hqta(var_rgwu)]
        var_wrnh = 0
        while var_wrnh < var_osiz(arg_xdvx):
            if arg_xdvx[var_wrnh] == '(':
                var_bacg.append(var_hqta(var_rgwu))
                var_wrnh += 1
            elif arg_xdvx[var_wrnh] == ')':
                var_ayzf = var_bacg.pop()
                var_wrnh += 1
                var_wnki = ''
                while var_wrnh < var_osiz(arg_xdvx) and arg_xdvx[var_wrnh
                    ].isdigit():
                    var_wnki += arg_xdvx[var_wrnh]
                    var_wrnh += 1
                if var_wnki:
                    var_wnki = var_rgwu(var_wnki)
                    for var_egyk in var_ayzf:
                        var_ayzf[var_egyk] *= var_wnki
                for var_egyk in var_ayzf:
                    var_bacg[-1][var_egyk] += var_ayzf[var_egyk]
            else:
                var_dcmd = arg_xdvx[var_wrnh]
                var_wrnh += 1
                while var_wrnh < var_osiz(arg_xdvx) and arg_xdvx[var_wrnh
                    ].islower():
                    var_dcmd += arg_xdvx[var_wrnh]
                    var_wrnh += 1
                var_llti = ''
                while var_wrnh < var_osiz(arg_xdvx) and arg_xdvx[var_wrnh
                    ].isdigit():
                    var_llti += arg_xdvx[var_wrnh]
                    var_wrnh += 1
                if var_llti == '':
                    var_bacg[-1][var_dcmd] += 1
                else:
                    var_bacg[-1][var_dcmd] += var_rgwu(var_llti)
        var_zbxo = var_rdmc(var_rjut(var_bacg[0].items()))
        var_lsgw = ''
        for var_egyk in var_zbxo:
            var_lsgw += var_egyk
            if var_zbxo[var_egyk] > 1:
                var_lsgw += var_rcsn(var_zbxo[var_egyk])
        return var_lsgw
