class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.total_ways = 0

    def func_xdvx(arg_ihhe, arg_rcsn: var_hqta[var_rgwu], arg_bacg: var_rgwu
        ) ->var_rgwu:
        arg_ihhe.calculate_ways(arg_rcsn, 0, 0, arg_bacg)
        return arg_ihhe.total_ways

    def func_wrnh(arg_ihhe, arg_rcsn: var_hqta[var_rgwu], arg_osiz:
        var_rgwu, arg_ayzf: var_rgwu, arg_bacg: var_rgwu):
        if arg_osiz == var_wnki(arg_rcsn):
            if arg_ayzf == arg_bacg:
                arg_ihhe.total_ways += 1
        else:
            arg_ihhe.calculate_ways(arg_rcsn, arg_osiz + 1, arg_ayzf +
                arg_rcsn[arg_osiz], arg_bacg)
            arg_ihhe.calculate_ways(arg_rcsn, arg_osiz + 1, arg_ayzf -
                arg_rcsn[arg_osiz], arg_bacg)
