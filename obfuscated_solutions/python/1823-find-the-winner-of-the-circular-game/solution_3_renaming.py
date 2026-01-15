class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        return arg_ihhe.winnerHelper(arg_xdvx, arg_rcsn) + 1

    def func_hqta(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        if arg_xdvx == 1:
            return 0
        return (arg_ihhe.winnerHelper(arg_xdvx - 1, arg_rcsn) + arg_rcsn
            ) % arg_xdvx
