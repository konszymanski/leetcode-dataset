class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(var_osiz % arg_rcsn for var_osiz in arg_xdvx)
        var_ayzf = 0
        while var_rgwu[var_ayzf % arg_rcsn] > 0:
            var_rgwu[var_ayzf % arg_rcsn] -= 1
            var_ayzf += 1
        return var_ayzf
