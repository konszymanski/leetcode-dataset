class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rdmc[var_wrnh]:
        var_hqta = var_rgwu(var_wrnh)
        var_osiz = var_ayzf([arg_xdvx])
        while var_osiz:
            var_wnki = var_osiz.popleft()
            var_hqta[var_wnki.val] += 1
            if var_wnki.left:
                var_osiz.append(var_wnki.left)
            if var_wnki.right:
                var_osiz.append(var_wnki.right)
        var_egyk = var_dcmd(var_hqta.values())
        var_llti = []
        for var_zbxo in var_hqta:
            if var_hqta[var_zbxo] == var_egyk:
                var_llti.append(var_zbxo)
        return var_llti
