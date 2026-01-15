class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = {}
        return arg_ihhe.helper(arg_xdvx, arg_rcsn, var_hqta)

    def func_rgwu(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg,
        var_hqta: var_wrnh) ->var_bacg:
        var_osiz = arg_xdvx, arg_rcsn
        if var_osiz in var_hqta:
            return var_hqta[var_osiz]
        if not arg_xdvx and not arg_rcsn:
            return ''
        if not arg_xdvx:
            return arg_rcsn
        if not arg_rcsn:
            return arg_xdvx
        if arg_xdvx[0] == arg_rcsn[0]:
            var_hqta[var_osiz] = arg_xdvx[0] + arg_ihhe.helper(arg_xdvx[1:],
                arg_rcsn[1:], var_hqta)
            return var_hqta[var_osiz]
        var_ayzf = arg_xdvx[0] + arg_ihhe.helper(arg_xdvx[1:], arg_rcsn,
            var_hqta)
        var_wnki = arg_rcsn[0] + arg_ihhe.helper(arg_xdvx, arg_rcsn[1:],
            var_hqta)
        var_hqta[var_osiz] = var_ayzf if var_egyk(var_ayzf) < var_egyk(var_wnki
            ) else var_wnki
        return var_hqta[var_osiz]
