class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg = 1000000007
        var_hqta = [([-1] * 3) for var_rgwu in var_wrnh(var_osiz(arg_xdvx) + 1)
            ]
        var_hqta[var_osiz(arg_xdvx)][0] = 0
        var_hqta[var_osiz(arg_xdvx)][1] = 0
        var_hqta[var_osiz(arg_xdvx)][2] = 1
        for var_ayzf in var_wrnh(var_osiz(arg_xdvx) - 1, -1, -1):
            if arg_xdvx[var_ayzf] == 'S':
                var_hqta[var_ayzf][0] = var_hqta[var_ayzf + 1][1]
                var_hqta[var_ayzf][1] = var_hqta[var_ayzf + 1][2]
                var_hqta[var_ayzf][2] = var_hqta[var_ayzf + 1][1]
            else:
                var_hqta[var_ayzf][0] = var_hqta[var_ayzf + 1][0]
                var_hqta[var_ayzf][1] = var_hqta[var_ayzf + 1][1]
                var_hqta[var_ayzf][2] = (var_hqta[var_ayzf + 1][0] +
                    var_hqta[var_ayzf + 1][2]) % var_bacg
        return var_hqta[0][0]
