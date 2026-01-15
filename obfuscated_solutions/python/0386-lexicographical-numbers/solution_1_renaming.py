class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh[var_rcsn]:
        var_bacg = []
        for var_hqta in var_rgwu(1, 10):
            arg_ihhe._generate_lexical_numbers(var_hqta, arg_xdvx, var_bacg)
        return var_bacg

    def func_osiz(arg_ihhe, arg_ayzf: var_rcsn, arg_wnki: var_rcsn,
        arg_egyk: var_wrnh[var_rcsn]):
        if arg_ayzf > arg_wnki:
            return
        arg_egyk.append(arg_ayzf)
        for var_dcmd in var_rgwu(10):
            var_llti = arg_ayzf * 10 + var_dcmd
            if var_llti <= arg_wnki:
                arg_ihhe._generate_lexical_numbers(var_llti, arg_wnki, arg_egyk
                    )
            else:
                break
