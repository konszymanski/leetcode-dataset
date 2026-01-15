class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_osiz:
        var_hqta = arg_rcsn & -arg_rcsn
        var_rgwu = arg_rcsn // var_hqta >> 1 & 1 == 1
        var_wrnh = arg_rcsn & 1 == 0
        if var_rgwu:
            return '0' if var_wrnh else '1'
        else:
            return '1' if var_wrnh else '0'
