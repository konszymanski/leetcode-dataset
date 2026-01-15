class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu, arg_hqta: var_rgwu) ->var_rgwu:
        var_wrnh = [1] + [0] * arg_rcsn
        var_osiz = 10 ** 9 + 7
        for var_ayzf in var_wnki(1, arg_rcsn + 1):
            if var_ayzf >= arg_bacg:
                var_wrnh[var_ayzf] += var_wrnh[var_ayzf - arg_bacg]
            if var_ayzf >= arg_hqta:
                var_wrnh[var_ayzf] += var_wrnh[var_ayzf - arg_hqta]
            var_wrnh[var_ayzf] %= var_osiz
        return var_egyk(var_wrnh[arg_xdvx:arg_rcsn + 1]) % var_osiz
