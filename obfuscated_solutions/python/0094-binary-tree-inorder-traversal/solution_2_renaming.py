class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = []
        var_bacg = []
        var_hqta = arg_xdvx
        while var_hqta or var_bacg:
            while var_hqta:
                var_bacg.append(var_hqta)
                var_hqta = var_hqta.left
            var_hqta = var_bacg.pop()
            var_rcsn.append(var_hqta.val)
            var_hqta = var_hqta.right
        return var_rcsn
