class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_rgwu]) ->var_wnki:
        var_wrnh = [arg_xdvx.val]
        var_osiz = [0]
        var_ayzf = 0
        arg_xdvx = arg_xdvx.next
        while arg_xdvx:
            while var_ayzf > 0 and arg_xdvx.val != var_wrnh[var_ayzf]:
                var_ayzf = var_osiz[var_ayzf - 1]
            var_ayzf += 1 if arg_xdvx.val == var_wrnh[var_ayzf] else 0
            var_wrnh.append(arg_xdvx.val)
            var_osiz.append(var_ayzf)
            arg_xdvx = arg_xdvx.next
        return arg_ihhe._search_in_tree(arg_rcsn, 0, var_wrnh, var_osiz)

    def func_egyk(arg_ihhe, arg_dcmd: var_bacg[var_rgwu], var_ayzf:
        var_llti, var_wrnh: var_zbxo[var_llti], var_osiz: var_zbxo[var_llti]
        ) ->var_wnki:
        if not arg_dcmd:
            return False
        while var_ayzf > 0 and arg_dcmd.val != var_wrnh[var_ayzf]:
            var_ayzf = var_osiz[var_ayzf - 1]
        var_ayzf += 1 if arg_dcmd.val == var_wrnh[var_ayzf] else 0
        if var_ayzf == var_rdmc(var_wrnh):
            return True
        return arg_ihhe._search_in_tree(arg_dcmd.left, var_ayzf, var_wrnh,
            var_osiz) or arg_ihhe._search_in_tree(arg_dcmd.right, var_ayzf,
            var_wrnh, var_osiz)
