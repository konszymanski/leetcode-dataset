class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta.namedtuple('Result', ('node', 'dist'))

        def func_rgwu(arg_wrnh):
            if not arg_wrnh:
                return var_bacg(None, 0)
            var_osiz, var_ayzf = func_rgwu(arg_wrnh.left), func_rgwu(arg_wrnh
                .right)
            if var_osiz.dist > var_ayzf.dist:
                return var_bacg(var_osiz.node, var_osiz.dist + 1)
            if var_osiz.dist < var_ayzf.dist:
                return var_bacg(var_ayzf.node, var_ayzf.dist + 1)
            return var_bacg(arg_wrnh, var_osiz.dist + 1)
        return func_rgwu(arg_rcsn).node
