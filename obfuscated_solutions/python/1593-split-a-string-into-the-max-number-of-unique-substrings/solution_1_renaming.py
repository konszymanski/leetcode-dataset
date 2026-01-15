class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rgwu:
        var_bacg = var_hqta()
        return arg_ihhe.backtrack(arg_xdvx, 0, var_bacg)

    def func_wrnh(arg_ihhe, arg_xdvx, arg_osiz, var_bacg):
        if arg_osiz == var_ayzf(arg_xdvx):
            return 0
        var_wnki = 0
        for var_egyk in var_dcmd(arg_osiz + 1, var_ayzf(arg_xdvx) + 1):
            var_llti = arg_xdvx[arg_osiz:var_egyk]
            if var_llti not in var_bacg:
                var_bacg.add(var_llti)
                var_wnki = var_zbxo(var_wnki, 1 + arg_ihhe.backtrack(
                    arg_xdvx, var_egyk, var_bacg))
                var_bacg.remove(var_llti)
        return var_wnki
