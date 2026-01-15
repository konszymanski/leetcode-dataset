class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = arg_xdvx
        var_hqta = None
        while var_bacg:
            var_rgwu = var_bacg.val * 2
            if var_rgwu < 10:
                var_bacg.val = var_rgwu
            elif var_hqta:
                var_bacg.val = var_rgwu % 10
                var_hqta.val += 1
            else:
                arg_xdvx = var_rcsn(1, var_bacg)
                var_bacg.val = var_rgwu % 10
            var_hqta = var_bacg
            var_bacg = var_bacg.next
        return arg_xdvx
