class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = 0
        var_ayzf = var_wnki(arg_xdvx)
        for var_egyk in var_dcmd(var_ayzf):
            if arg_xdvx[var_egyk] == 'N':
                var_rgwu += 1
            elif arg_xdvx[var_egyk] == 'S':
                var_rgwu -= 1
            elif arg_xdvx[var_egyk] == 'E':
                var_wrnh += 1
            elif arg_xdvx[var_egyk] == 'W':
                var_wrnh -= 1
            var_osiz = var_llti(var_osiz, var_zbxo(var_rdmc(var_rgwu) +
                var_rdmc(var_wrnh) + arg_rcsn * 2, var_egyk + 1))
        return var_osiz
