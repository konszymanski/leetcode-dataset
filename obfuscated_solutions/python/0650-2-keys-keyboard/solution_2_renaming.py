class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        if arg_xdvx == 1:
            return 0
        arg_ihhe.n = arg_xdvx
        arg_ihhe.memo = [([0] * (arg_xdvx // 2 + 1)) for var_bacg in
            var_hqta(arg_xdvx + 1)]
        return 1 + arg_ihhe._min_steps_helper(1, 1)

    def func_rgwu(arg_ihhe, arg_wrnh: var_rcsn, arg_osiz: var_rcsn) ->var_rcsn:
        if arg_wrnh == arg_ihhe.n:
            return 0
        if arg_wrnh > arg_ihhe.n:
            return 1000
        if arg_ihhe.memo[arg_wrnh][arg_osiz] != 0:
            return arg_ihhe.memo[arg_wrnh][arg_osiz]
        var_ayzf = 1 + arg_ihhe._min_steps_helper(arg_wrnh + arg_osiz, arg_osiz
            )
        var_wnki = 2 + arg_ihhe._min_steps_helper(arg_wrnh * 2, arg_wrnh)
        arg_ihhe.memo[arg_wrnh][arg_osiz] = var_egyk(var_ayzf, var_wnki)
        return arg_ihhe.memo[arg_wrnh][arg_osiz]
