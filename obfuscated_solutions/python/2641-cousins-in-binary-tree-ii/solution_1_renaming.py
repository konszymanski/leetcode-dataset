class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        if not arg_xdvx:
            return arg_xdvx
        var_rcsn = var_bacg([arg_xdvx])
        var_hqta = []
        while var_rcsn:
            var_rgwu = 0
            var_wrnh = var_osiz(var_rcsn)
            for var_ayzf in var_wnki(var_wrnh):
                var_egyk = var_rcsn.popleft()
                var_rgwu += var_egyk.val
                if var_egyk.left:
                    var_rcsn.append(var_egyk.left)
                if var_egyk.right:
                    var_rcsn.append(var_egyk.right)
            var_hqta.append(var_rgwu)
        var_rcsn.append(arg_xdvx)
        var_dcmd = 1
        arg_xdvx.val = 0
        while var_rcsn:
            var_wrnh = var_osiz(var_rcsn)
            for var_ayzf in var_wnki(var_wrnh):
                var_egyk = var_rcsn.popleft()
                var_llti = (var_egyk.left.val if var_egyk.left else 0) + (
                    var_egyk.right.val if var_egyk.right else 0)
                if var_egyk.left:
                    var_egyk.left.val = var_hqta[var_dcmd] - var_llti
                    var_rcsn.append(var_egyk.left)
                if var_egyk.right:
                    var_egyk.right.val = var_hqta[var_dcmd] - var_llti
                    var_rcsn.append(var_egyk.right)
            var_dcmd += 1
        return arg_xdvx
