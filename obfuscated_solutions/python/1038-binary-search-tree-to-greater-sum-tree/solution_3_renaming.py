class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 0
        var_hqta = []
        var_rgwu = arg_xdvx
        while var_hqta or var_rgwu is not None:
            while var_rgwu is not None:
                var_hqta.append(var_rgwu)
                var_rgwu = var_rgwu.right
            var_rgwu = var_hqta.pop()
            var_bacg += var_rgwu.val
            var_rgwu.val = var_bacg
            var_rgwu = var_rgwu.left
        return arg_xdvx
