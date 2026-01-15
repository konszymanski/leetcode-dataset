class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = 1
        arg_bacg -= 1
        while arg_bacg > 0:
            var_rgwu = arg_xdvx._count_steps(arg_rcsn, var_hqta, var_hqta + 1)
            if var_rgwu <= arg_bacg:
                var_hqta += 1
                arg_bacg -= var_rgwu
            else:
                var_hqta *= 10
                arg_bacg -= 1
        return var_hqta

    def func_wrnh(arg_xdvx, arg_rcsn, arg_osiz, arg_ayzf):
        var_wnki = 0
        while arg_osiz <= arg_rcsn:
            var_wnki += var_egyk(arg_rcsn + 1, arg_ayzf) - arg_osiz
            arg_osiz *= 10
            arg_ayzf *= 10
        return var_wnki
