class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_rdmc:
        var_rgwu = var_wrnh(arg_rcsn)
        var_osiz = var_ayzf([0])
        var_wnki = var_wrnh()
        while var_osiz:
            var_egyk = var_osiz.popleft()
            if var_egyk == var_dcmd(arg_xdvx):
                return True
            for var_llti in var_zbxo(var_egyk + 1, var_dcmd(arg_xdvx) + 1):
                if var_llti in var_wnki:
                    continue
                if arg_xdvx[var_egyk:var_llti] in var_rgwu:
                    var_osiz.append(var_llti)
                    var_wnki.add(var_llti)
        return False
