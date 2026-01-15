class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = []
        arg_xdvx.sort(key=lambda x: var_rgwu[0])
        var_wrnh = 0
        var_osiz = 0
        for var_ayzf in arg_xdvx:
            while var_hqta and var_hqta[0][0] < var_ayzf[0]:
                var_wrnh = var_wnki(var_wrnh, var_hqta[0][1])
                var_egyk.heappop(var_hqta)
            var_osiz = var_wnki(var_osiz, var_wrnh + var_ayzf[2])
            var_egyk.heappush(var_hqta, (var_ayzf[1], var_ayzf[2]))
        return var_osiz
