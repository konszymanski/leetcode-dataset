class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        if arg_xdvx is None:
            return arg_xdvx
        var_rcsn = var_bacg()
        var_rcsn.append(arg_xdvx)
        var_hqta = arg_xdvx.val
        while var_rcsn:
            var_rgwu = var_wrnh(var_rcsn)
            var_osiz = 0
            for var_ayzf in var_wnki(var_rgwu):
                var_egyk = var_rcsn.popleft()
                var_egyk.val = var_hqta - var_egyk.val
                var_dcmd = (0 if var_egyk.left is None else var_egyk.left.val
                    ) + (0 if var_egyk.right is None else var_egyk.right.val)
                if var_egyk.left is not None:
                    var_osiz += var_egyk.left.val
                    var_egyk.left.val = var_dcmd
                    var_rcsn.append(var_egyk.left)
                if var_egyk.right is not None:
                    var_osiz += var_egyk.right.val
                    var_egyk.right.val = var_dcmd
                    var_rcsn.append(var_egyk.right)
            var_hqta = var_osiz
        return arg_xdvx
