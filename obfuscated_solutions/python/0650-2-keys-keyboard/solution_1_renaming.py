class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.n = 0

    def func_xdvx(arg_ihhe, arg_rcsn, arg_bacg):
        if arg_rcsn == arg_ihhe.n:
            return 0
        if arg_rcsn > arg_ihhe.n:
            return 1000
        var_hqta = 2 + arg_ihhe._min_steps_helper(arg_rcsn * 2, arg_rcsn)
        var_rgwu = 1 + arg_ihhe._min_steps_helper(arg_rcsn + arg_bacg, arg_bacg
            )
        return var_wrnh(var_hqta, var_rgwu)

    def func_osiz(arg_ihhe, arg_ayzf: var_wnki) ->var_wnki:
        if arg_ayzf == 1:
            return 0
        arg_ihhe.n = arg_ayzf
        return 1 + arg_ihhe._min_steps_helper(1, 1)
