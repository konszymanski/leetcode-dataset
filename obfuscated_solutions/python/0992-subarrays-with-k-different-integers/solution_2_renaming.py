class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = [0] * (var_wrnh(arg_xdvx) + 1)
        var_osiz = 0
        var_ayzf = 0
        var_wnki = 0
        var_egyk = 0
        while var_wnki < var_wrnh(arg_xdvx):
            var_rgwu[arg_xdvx[var_wnki]] += 1
            if var_rgwu[arg_xdvx[var_wnki]] == 1:
                arg_rcsn -= 1
            if arg_rcsn < 0:
                var_rgwu[arg_xdvx[var_ayzf]] -= 1
                if var_rgwu[arg_xdvx[var_ayzf]] == 0:
                    arg_rcsn += 1
                var_ayzf += 1
                var_egyk = 0
            if arg_rcsn == 0:
                while var_rgwu[arg_xdvx[var_ayzf]] > 1:
                    var_rgwu[arg_xdvx[var_ayzf]] -= 1
                    var_ayzf += 1
                    var_egyk += 1
                var_osiz += var_egyk + 1
            var_wnki += 1
        return var_osiz
