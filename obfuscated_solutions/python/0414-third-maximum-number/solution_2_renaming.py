class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = []
        var_rgwu = var_wrnh()
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            if arg_xdvx[var_osiz] in var_rgwu:
                continue
            if var_wnki(var_hqta) == 3:
                if var_hqta[0] < arg_xdvx[var_osiz]:
                    var_rgwu.remove(var_hqta[0])
                    var_egyk(var_hqta)
                    var_dcmd(var_hqta, arg_xdvx[var_osiz])
                    var_rgwu.add(arg_xdvx[var_osiz])
            else:
                var_dcmd(var_hqta, arg_xdvx[var_osiz])
                var_rgwu.add(arg_xdvx[var_osiz])
        if var_wnki(var_hqta) == 1:
            return var_hqta[0]
        elif var_wnki(var_hqta) == 2:
            var_llti = var_hqta[0]
            var_egyk(var_hqta)
            return var_zbxo(var_llti, var_hqta[0])
        return var_hqta[0]
