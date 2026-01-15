class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 10 ** 9 + 7
        var_rgwu = var_wrnh = 0
        var_osiz = 0
        var_ayzf = 1
        for var_wnki in arg_xdvx:
            var_wrnh += var_wnki
            if var_wrnh % 2 == 0:
                var_rgwu += var_osiz
                var_ayzf += 1
            else:
                var_rgwu += var_ayzf
                var_osiz += 1
            var_rgwu %= var_hqta
        return var_rgwu
