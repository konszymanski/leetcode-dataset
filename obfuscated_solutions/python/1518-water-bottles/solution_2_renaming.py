class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 0
        while arg_xdvx >= arg_rcsn:
            var_rgwu = arg_xdvx // arg_rcsn
            var_hqta += arg_rcsn * var_rgwu
            arg_xdvx -= arg_rcsn * var_rgwu
            arg_xdvx += var_rgwu
        return var_hqta + arg_xdvx
