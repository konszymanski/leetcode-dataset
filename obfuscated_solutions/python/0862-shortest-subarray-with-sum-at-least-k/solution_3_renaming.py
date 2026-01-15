class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * (var_rgwu + 1)
        for var_ayzf in var_wnki(1, var_rgwu + 1):
            var_osiz[var_ayzf] = var_osiz[var_ayzf - 1] + arg_xdvx[var_ayzf - 1
                ]
        var_egyk = var_dcmd()
        var_llti = var_zbxo('inf')
        for var_ayzf in var_wnki(var_rgwu + 1):
            while var_egyk and var_osiz[var_ayzf] - var_osiz[var_egyk[0]
                ] >= arg_rcsn:
                var_llti = var_rdmc(var_llti, var_ayzf - var_egyk.popleft())
            while var_egyk and var_osiz[var_ayzf] <= var_osiz[var_egyk[-1]]:
                var_egyk.pop()
            var_egyk.append(var_ayzf)
        return var_llti if var_llti != var_zbxo('inf') else -1
