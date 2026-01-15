class Solution:
    var_udax = 1000
    var_ihhe = [0] * (var_udax + 1)

    def func_xdvx(arg_rcsn, arg_bacg: var_hqta) ->var_hqta:
        if arg_rcsn.precompute[1] == 0:
            for var_rgwu in var_wrnh(1, arg_rcsn.maxValue + 1):
                var_osiz = var_rgwu * (var_rgwu + 1) // 2
                var_ayzf = 1
                while var_ayzf * var_ayzf < var_osiz:
                    var_ayzf += 1
                arg_rcsn.precompute[var_rgwu
                    ] = var_ayzf if var_ayzf * var_ayzf == var_osiz else -1
        return arg_rcsn.precompute[arg_bacg]
