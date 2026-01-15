class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_rgwu[var_wrnh]) ->var_rgwu[var_hqta]:
        if not arg_xdvx:
            return []
        var_osiz = var_ayzf(arg_rcsn)
        var_wnki = []
        var_egyk = var_dcmd([arg_xdvx])
        while var_egyk:
            var_llti = var_egyk.popleft()
            if var_llti.left:
                var_egyk.append(var_llti.left)
                if var_llti.left.val in var_osiz:
                    var_llti.left = None
            if var_llti.right:
                var_egyk.append(var_llti.right)
                if var_llti.right.val in var_osiz:
                    var_llti.right = None
            if var_llti.val in var_osiz:
                if var_llti.left:
                    var_wnki.append(var_llti.left)
                if var_llti.right:
                    var_wnki.append(var_llti.right)
        if arg_xdvx.val not in var_osiz:
            var_wnki.append(arg_xdvx)
        return var_wnki
