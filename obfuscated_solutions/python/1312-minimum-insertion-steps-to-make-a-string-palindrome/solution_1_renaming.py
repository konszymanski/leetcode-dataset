class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_wrnh, arg_rcsn: var_wrnh,
        arg_bacg: var_osiz, arg_hqta: var_osiz, arg_rgwu: [[var_osiz]]
        ) ->var_osiz:
        if arg_bacg == 0 or arg_hqta == 0:
            return 0
        if arg_rgwu[arg_bacg][arg_hqta] != -1:
            return arg_rgwu[arg_bacg][arg_hqta]
        if arg_xdvx[arg_bacg - 1] == arg_rcsn[arg_hqta - 1]:
            return 1 + arg_ihhe.lcs(arg_xdvx, arg_rcsn, arg_bacg - 1, 
                arg_hqta - 1, arg_rgwu)
        return var_ayzf(arg_ihhe.lcs(arg_xdvx, arg_rcsn, arg_bacg - 1,
            arg_hqta, arg_rgwu), arg_ihhe.lcs(arg_xdvx, arg_rcsn, arg_bacg,
            arg_hqta - 1, arg_rgwu))

    def func_wnki(arg_ihhe, arg_egyk: var_wrnh) ->var_osiz:
        arg_hqta = var_dcmd(arg_egyk)
        var_llti = arg_egyk[::-1]
        arg_rgwu = [([-1] * (arg_hqta + 1)) for var_zbxo in var_rdmc(
            arg_hqta + 1)]
        return arg_hqta - arg_ihhe.lcs(arg_egyk, var_llti, arg_hqta,
            arg_hqta, arg_rgwu)
