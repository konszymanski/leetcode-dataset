class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_rgwu[var_wrnh]) ->var_rgwu[var_hqta]:
        var_osiz = var_ayzf(arg_rcsn)
        var_wnki = []
        arg_xdvx = arg_ihhe._process_node(arg_xdvx, var_osiz, var_wnki)
        if arg_xdvx:
            var_wnki.append(arg_xdvx)
        return var_wnki

    def func_egyk(arg_ihhe, arg_dcmd: var_hqta, var_osiz: var_llti[var_wrnh
        ], var_wnki: var_rgwu[var_hqta]) ->var_hqta:
        if not arg_dcmd:
            return None
        arg_dcmd.left = arg_ihhe._process_node(arg_dcmd.left, var_osiz,
            var_wnki)
        arg_dcmd.right = arg_ihhe._process_node(arg_dcmd.right, var_osiz,
            var_wnki)
        if arg_dcmd.val in var_osiz:
            if arg_dcmd.left:
                var_wnki.append(arg_dcmd.left)
            if arg_dcmd.right:
                var_wnki.append(arg_dcmd.right)
            return None
        return arg_dcmd
