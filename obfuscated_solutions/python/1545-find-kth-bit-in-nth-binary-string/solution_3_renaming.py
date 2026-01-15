class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_wrnh:
        var_hqta = 0
        var_rgwu = (1 << arg_xdvx) - 1
        while arg_rcsn > 1:
            if arg_rcsn == var_rgwu // 2 + 1:
                return '1' if var_hqta % 2 == 0 else '0'
            if arg_rcsn > var_rgwu // 2:
                arg_rcsn = var_rgwu + 1 - arg_rcsn
                var_hqta += 1
            var_rgwu //= 2
        return '0' if var_hqta % 2 == 0 else '1'
