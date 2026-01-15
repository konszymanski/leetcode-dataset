class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_llti:
        var_bacg = 1000000007
        var_hqta = []
        for var_rgwu, var_wrnh in var_osiz(arg_xdvx):
            if var_wrnh == 'S':
                var_hqta.append(var_rgwu)
        if var_hqta == [] or var_ayzf(var_hqta) % 2 == 1:
            return 0
        var_wnki = 1
        var_egyk = 1
        var_dcmd = 2
        while var_dcmd < var_ayzf(var_hqta):
            var_wnki *= var_hqta[var_dcmd] - var_hqta[var_egyk]
            var_wnki %= var_bacg
            var_egyk += 2
            var_dcmd += 2
        return var_wnki
