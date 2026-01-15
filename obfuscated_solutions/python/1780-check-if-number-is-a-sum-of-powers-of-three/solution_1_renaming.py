class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_bacg:
        return arg_ihhe._check_powers_of_three_helper(0, arg_xdvx)

    def func_hqta(arg_ihhe, arg_rgwu: var_rcsn, arg_xdvx: var_rcsn) ->var_bacg:
        if arg_xdvx == 0:
            return True
        if 3 ** arg_rgwu > arg_xdvx:
            return False
        var_wrnh = arg_ihhe._check_powers_of_three_helper(arg_rgwu + 1, 
            arg_xdvx - 3 ** arg_rgwu)
        var_osiz = arg_ihhe._check_powers_of_three_helper(arg_rgwu + 1,
            arg_xdvx)
        return var_wrnh or var_osiz
