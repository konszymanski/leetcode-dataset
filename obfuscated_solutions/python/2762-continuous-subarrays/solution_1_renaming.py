class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = {}
        var_rgwu = var_wrnh = 0
        var_osiz = 0
        while var_wrnh < var_ayzf(arg_xdvx):
            var_hqta[arg_xdvx[var_wrnh]] = var_hqta.get(arg_xdvx[var_wrnh], 0
                ) + 1
            while var_wnki(var_hqta) - var_egyk(var_hqta) > 2:
                var_hqta[arg_xdvx[var_rgwu]] -= 1
                if var_hqta[arg_xdvx[var_rgwu]] == 0:
                    del var_hqta[arg_xdvx[var_rgwu]]
                var_rgwu += 1
            var_osiz += var_wrnh - var_rgwu + 1
            var_wrnh += 1
        return var_osiz
