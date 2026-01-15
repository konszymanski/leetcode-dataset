class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_egyk:
        var_rgwu = 0
        arg_xdvx -= 1
        for var_wrnh in var_osiz(arg_xdvx.bit_length() - 1, -1, -1):
            if arg_xdvx >> var_wrnh & 1:
                var_rgwu += arg_rcsn[var_wrnh]
        return var_ayzf(var_wnki('a') + var_rgwu % 26)
