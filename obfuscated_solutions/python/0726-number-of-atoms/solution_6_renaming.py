class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = []
        var_hqta = 1
        var_rgwu = [1]
        var_wrnh = var_osiz(arg_xdvx) - 1
        var_ayzf = ''
        while var_wrnh >= 0:
            if arg_xdvx[var_wrnh].isdigit():
                var_ayzf += arg_xdvx[var_wrnh]
            elif arg_xdvx[var_wrnh].isalpha():
                var_ayzf = ''
            elif arg_xdvx[var_wrnh] == ')':
                var_wnki = var_egyk(var_ayzf[::-1]) if var_ayzf else 1
                var_hqta *= var_wnki
                var_rgwu.append(var_wnki)
                var_ayzf = ''
            elif arg_xdvx[var_wrnh] == '(':
                var_hqta //= var_rgwu.pop()
                var_ayzf = ''
            var_bacg.append(var_hqta)
            var_wrnh -= 1
        var_bacg = var_bacg[::-1]
        var_dcmd = var_llti(var_egyk)
        var_wrnh = 0
        while var_wrnh < var_osiz(arg_xdvx):
            if arg_xdvx[var_wrnh].isupper():
                var_zbxo = arg_xdvx[var_wrnh]
                var_rdmc = ''
                var_wrnh += 1
                while var_wrnh < var_osiz(arg_xdvx) and arg_xdvx[var_wrnh
                    ].islower():
                    var_zbxo += arg_xdvx[var_wrnh]
                    var_wrnh += 1
                while var_wrnh < var_osiz(arg_xdvx) and arg_xdvx[var_wrnh
                    ].isdigit():
                    var_rdmc += arg_xdvx[var_wrnh]
                    var_wrnh += 1
                if var_rdmc:
                    var_dcmd[var_zbxo] += var_egyk(var_rdmc) * var_bacg[
                        var_wrnh - 1]
                else:
                    var_dcmd[var_zbxo] += 1 * var_bacg[var_wrnh - 1]
            else:
                var_wrnh += 1
        var_dcmd = var_rjut(var_lsgw(var_dcmd.items()))
        var_cbvh = ''
        for var_yjch in var_dcmd:
            var_cbvh += var_yjch
            if var_dcmd[var_yjch] > 1:
                var_cbvh += var_rcsn(var_dcmd[var_yjch])
        return var_cbvh
