class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rjut[var_lsgw]:
        if not arg_xdvx:
            return []
        var_hqta = []
        var_rgwu = var_wrnh([arg_xdvx])
        while var_rgwu:
            var_osiz = var_ayzf(var_rgwu)
            var_wnki = var_egyk('-inf')
            for var_dcmd in var_llti(var_osiz):
                var_zbxo = var_rgwu.popleft()
                var_wnki = var_rdmc(var_wnki, var_zbxo.val)
                if var_zbxo.left:
                    var_rgwu.append(var_zbxo.left)
                if var_zbxo.right:
                    var_rgwu.append(var_zbxo.right)
            var_hqta.append(var_wnki)
        return var_hqta
