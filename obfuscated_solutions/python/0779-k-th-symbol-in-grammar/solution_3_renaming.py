class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        if arg_xdvx == 1:
            return 0
        var_hqta = 1
        for var_rgwu in var_wrnh(arg_xdvx, 1, -1):
            var_osiz = 2 ** (var_rgwu - 1)
            var_ayzf = var_osiz // 2
            if arg_rcsn > var_ayzf:
                var_hqta = 1 - var_hqta
                arg_rcsn -= var_ayzf
        if var_hqta != 0:
            return 0
        return 1
