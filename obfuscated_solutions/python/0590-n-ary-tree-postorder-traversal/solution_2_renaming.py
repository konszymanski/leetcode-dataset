class Solution:

    def func_udax(arg_ihhe, arg_xdvx: 'Node') ->var_wrnh[var_osiz]:
        var_rcsn = []
        if arg_xdvx is None:
            return var_rcsn
        var_bacg = [arg_xdvx]
        while var_bacg:
            var_hqta = var_bacg.pop()
            var_rcsn.append(var_hqta.val)
            for var_rgwu in var_hqta.children:
                var_bacg.append(var_rgwu)
        var_rcsn.reverse()
        return var_rcsn
