class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu,
        arg_bacg: var_hqta) ->var_egyk[var_hqta]:
        var_wrnh = []
        var_osiz = var_ayzf(arg_xdvx)
        var_wnki = 0
        while var_wnki < var_osiz:
            var_wrnh.append(arg_xdvx[var_wnki:var_wnki + arg_rcsn])
            var_wnki += arg_rcsn
        var_wrnh[-1] += arg_bacg * (arg_rcsn - var_ayzf(var_wrnh[-1]))
        return var_wrnh
