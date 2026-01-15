class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        if arg_xdvx == 0:
            return 0
        var_bacg = 0
        var_hqta = 1
        while var_hqta * 2 <= arg_xdvx:
            var_hqta *= 2
            var_bacg += 1
        return 2 ** (var_bacg + 1) - 1 - arg_ihhe.minimumOneBitOperations(
            arg_xdvx ^ var_hqta)
