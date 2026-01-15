class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_zbxo[var_wrnh]:
        var_hqta = var_rgwu(var_wrnh)
        var_osiz = [arg_xdvx]
        while var_osiz:
            var_ayzf = var_osiz.pop()
            var_hqta[var_ayzf.val] += 1
            if var_ayzf.left:
                var_osiz.append(var_ayzf.left)
            if var_ayzf.right:
                var_osiz.append(var_ayzf.right)
        var_wnki = var_egyk(var_hqta.values())
        var_dcmd = []
        for var_llti in var_hqta:
            if var_hqta[var_llti] == var_wnki:
                var_dcmd.append(var_llti)
        return var_dcmd
