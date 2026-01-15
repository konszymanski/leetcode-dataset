class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        while arg_rcsn in arg_xdvx:
            var_hqta = arg_xdvx.find(arg_rcsn)
            arg_xdvx = arg_xdvx[:var_hqta] + arg_xdvx[var_hqta + var_rgwu(
                arg_rcsn):]
        return arg_xdvx
