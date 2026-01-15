class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_osiz:
        var_hqta = ''
        var_rgwu = []
        arg_ihhe.generate_happy_strings(arg_xdvx, var_hqta, var_rgwu)
        if var_wrnh(var_rgwu) < arg_rcsn:
            return ''
        return var_rgwu[arg_rcsn - 1]

    def func_ayzf(arg_ihhe, arg_xdvx: var_bacg, var_hqta: var_osiz,
        var_rgwu: var_wnki):
        if var_wrnh(var_hqta) == arg_xdvx:
            var_rgwu.append(var_hqta)
            return
        for var_egyk in ['a', 'b', 'c']:
            if var_wrnh(var_hqta) > 0 and var_hqta[-1] == var_egyk:
                continue
            arg_ihhe.generate_happy_strings(arg_xdvx, var_hqta + var_egyk,
                var_rgwu)
