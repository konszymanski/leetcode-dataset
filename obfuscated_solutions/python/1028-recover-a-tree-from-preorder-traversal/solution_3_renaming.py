class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_zbxo[var_dcmd]:
        var_bacg = []
        var_hqta, var_rgwu = 0, var_wrnh(arg_xdvx)
        while var_hqta < var_rgwu:
            var_osiz = 0
            while var_hqta < var_rgwu and arg_xdvx[var_hqta] == '-':
                var_osiz += 1
                var_hqta += 1
            var_ayzf = 0
            while var_hqta < var_rgwu and arg_xdvx[var_hqta].isdigit():
                var_ayzf = var_ayzf * 10 + var_wnki(arg_xdvx[var_hqta])
                var_hqta += 1
            var_egyk = var_dcmd(var_ayzf)
            if var_osiz < var_wrnh(var_bacg):
                var_bacg[var_osiz] = var_egyk
            else:
                var_bacg.append(var_egyk)
            if var_osiz > 0:
                var_llti = var_bacg[var_osiz - 1]
                if var_llti.left is None:
                    var_llti.left = var_egyk
                else:
                    var_llti.right = var_egyk
        return var_bacg[0]
