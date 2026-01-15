class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        if not arg_xdvx or not arg_xdvx[0]:
            return []
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz, var_ayzf = 0, 0
        var_wnki = 1
        var_egyk = []
        while var_osiz < var_hqta and var_ayzf < var_rgwu:
            var_egyk.append(arg_xdvx[var_osiz][var_ayzf])
            var_dcmd = var_osiz + (-1 if var_wnki == 1 else 1)
            var_llti = var_ayzf + (1 if var_wnki == 1 else -1)
            if (var_dcmd < 0 or var_dcmd == var_hqta or var_llti < 0 or 
                var_llti == var_rgwu):
                if var_wnki:
                    var_osiz += var_ayzf == var_rgwu - 1
                    var_ayzf += var_ayzf < var_rgwu - 1
                else:
                    var_ayzf += var_osiz == var_hqta - 1
                    var_osiz += var_osiz < var_hqta - 1
                var_wnki = 1 - var_wnki
            else:
                var_osiz = var_dcmd
                var_ayzf = var_llti
        return var_egyk
