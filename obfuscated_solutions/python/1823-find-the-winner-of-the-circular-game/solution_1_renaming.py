class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = var_rgwu(var_wrnh(1, arg_xdvx + 1))
        var_osiz = 0
        while var_ayzf(var_hqta) > 1:
            var_wnki = (var_osiz + arg_rcsn - 1) % var_ayzf(var_hqta)
            var_hqta.pop(var_wnki)
            var_osiz = var_wnki
        return var_hqta[0]
