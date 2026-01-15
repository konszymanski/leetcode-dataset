class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = var_wrnh()
        var_osiz = 0
        for var_ayzf in var_wnki(arg_rcsn):
            var_egyk = arg_xdvx[var_ayzf]
            if var_egyk == 'W':
                var_osiz += 1
            var_rgwu.append(var_egyk)
        var_dcmd = var_osiz
        for var_ayzf in var_wnki(arg_rcsn, var_llti(arg_xdvx)):
            if var_rgwu.popleft() == 'W':
                var_osiz -= 1
            var_egyk = arg_xdvx[var_ayzf]
            if var_egyk == 'W':
                var_osiz += 1
            var_rgwu.append(var_egyk)
            var_dcmd = var_zbxo(var_dcmd, var_osiz)
        return var_dcmd
