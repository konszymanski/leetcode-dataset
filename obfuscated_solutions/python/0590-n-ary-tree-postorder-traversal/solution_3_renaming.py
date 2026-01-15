class Solution:

    def func_udax(arg_ihhe, arg_xdvx: 'Node') ->var_osiz[var_ayzf]:
        var_rcsn = []
        if arg_xdvx is None:
            return var_rcsn
        var_bacg = [arg_xdvx]
        var_hqta = []
        while var_bacg:
            var_rgwu = var_bacg.pop()
            var_hqta.append(var_rgwu)
            for var_wrnh in var_rgwu.children:
                var_bacg.append(var_wrnh)
        while var_hqta:
            var_rgwu = var_hqta.pop()
            var_rcsn.append(var_rgwu.val)
        return var_rcsn
