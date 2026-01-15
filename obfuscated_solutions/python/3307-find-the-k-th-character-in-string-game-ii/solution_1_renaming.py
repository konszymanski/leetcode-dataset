class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_wnki:
        var_rgwu = 0
        while arg_xdvx != 1:
            var_wrnh = arg_xdvx.bit_length() - 1
            if 1 << var_wrnh == arg_xdvx:
                var_wrnh -= 1
            arg_xdvx -= 1 << var_wrnh
            if arg_rcsn[var_wrnh]:
                var_rgwu += 1
        return var_osiz(var_ayzf('a') + var_rgwu % 26)
