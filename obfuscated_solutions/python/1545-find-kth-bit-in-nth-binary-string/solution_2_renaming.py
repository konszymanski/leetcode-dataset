class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_wrnh:
        if arg_xdvx == 1:
            return '0'
        var_hqta = 1 << arg_xdvx
        if arg_rcsn < var_hqta // 2:
            return arg_ihhe.findKthBit(arg_xdvx - 1, arg_rcsn)
        elif arg_rcsn == var_hqta // 2:
            return '1'
        else:
            var_rgwu = arg_ihhe.findKthBit(arg_xdvx - 1, var_hqta - arg_rcsn)
            return '1' if var_rgwu == '0' else '0'
