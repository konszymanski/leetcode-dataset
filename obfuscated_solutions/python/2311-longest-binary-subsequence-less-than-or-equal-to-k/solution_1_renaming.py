class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = arg_rcsn.bit_length()
        for var_ayzf, var_wnki in var_egyk(arg_xdvx[::-1]):
            if var_wnki == '1':
                if var_ayzf < var_osiz and var_rgwu + (1 << var_ayzf
                    ) <= arg_rcsn:
                    var_rgwu += 1 << var_ayzf
                    var_wrnh += 1
            else:
                var_wrnh += 1
        return var_wrnh
