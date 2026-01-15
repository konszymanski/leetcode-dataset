class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.count = 0

    def func_xdvx(arg_ihhe, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = [var_rgwu for var_rgwu in var_wrnh(1, arg_rcsn + 1)]
        arg_ihhe.permute(var_hqta, 0)
        return arg_ihhe.count

    def func_osiz(arg_ihhe, var_hqta, arg_ayzf):
        if arg_ayzf == var_wnki(var_hqta) - 1:
            for var_rgwu in var_wrnh(1, var_wnki(var_hqta) + 1):
                if var_hqta[var_rgwu - 1
                    ] % var_rgwu != 0 and var_rgwu % var_hqta[var_rgwu - 1
                    ] != 0:
                    break
            else:
                arg_ihhe.count += 1
        for var_rgwu in var_wrnh(arg_ayzf, var_wnki(var_hqta)):
            var_hqta[var_rgwu], var_hqta[arg_ayzf] = var_hqta[arg_ayzf
                ], var_hqta[var_rgwu]
            arg_ihhe.permute(var_hqta, arg_ayzf + 1)
            var_hqta[var_rgwu], var_hqta[arg_ayzf] = var_hqta[arg_ayzf
                ], var_hqta[var_rgwu]
