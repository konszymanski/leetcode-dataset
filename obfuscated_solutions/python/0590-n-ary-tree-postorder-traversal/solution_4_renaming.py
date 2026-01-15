class Solution:

    def func_udax(arg_ihhe, arg_xdvx: 'Node') ->var_ayzf[var_wnki]:
        var_rcsn = []
        if arg_xdvx is None:
            return var_rcsn
        var_bacg = [(arg_xdvx, False)]
        while var_bacg:
            var_hqta, var_rgwu = var_bacg.pop()
            if var_rgwu:
                var_rcsn.append(var_hqta.val)
            else:
                var_bacg.append((var_hqta, True))
                for var_wrnh in var_osiz(var_hqta.children):
                    var_bacg.append((var_wrnh, False))
        return var_rcsn
