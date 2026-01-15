class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        if not arg_xdvx:
            return None
        var_rcsn = [arg_xdvx]
        var_bacg = 0
        while var_rcsn:
            var_hqta = var_rgwu(var_rcsn)
            var_wrnh = []
            for var_osiz in var_ayzf(var_hqta):
                var_wnki = var_rcsn.pop(0)
                var_wrnh.append(var_wnki)
                if var_wnki.left:
                    var_rcsn.append(var_wnki.left)
                if var_wnki.right:
                    var_rcsn.append(var_wnki.right)
            if var_bacg % 2 == 1:
                var_egyk, var_dcmd = 0, var_rgwu(var_wrnh) - 1
                while var_egyk < var_dcmd:
                    var_llti = var_wrnh[var_egyk].val
                    var_wrnh[var_egyk].val = var_wrnh[var_dcmd].val
                    var_wrnh[var_dcmd].val = var_llti
                    var_egyk += 1
                    var_dcmd -= 1
            var_bacg += 1
        return arg_xdvx
