class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_rgwu
        ) ->var_bacg[var_hqta]:
        if not arg_xdvx:
            return None
        var_wrnh = []
        var_osiz = arg_xdvx
        var_ayzf = None
        while var_wrnh or var_osiz:
            while var_osiz:
                var_wrnh.append(var_osiz)
                var_osiz = var_osiz.left
            var_osiz = var_wrnh[-1]
            if var_osiz.right and var_osiz.right is not var_ayzf:
                var_osiz = var_osiz.right
                continue
            var_wrnh.pop()
            if (not var_osiz.right and not var_osiz.left and var_osiz.val ==
                arg_rcsn):
                if not var_wrnh:
                    return None
                var_wnki = var_wrnh[-1] if var_wrnh else None
                if var_wnki and var_wnki.left is var_osiz:
                    var_wnki.left = None
                elif var_wnki and var_wnki.right is var_osiz:
                    var_wnki.right = None
            var_ayzf = var_osiz
            var_osiz = None
        return arg_xdvx
