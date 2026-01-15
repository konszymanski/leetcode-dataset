class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [[] for var_osiz in var_ayzf(var_hqta)]
        for var_wnki in var_ayzf(var_hqta):
            for var_egyk in var_ayzf(var_wnki + 1, var_hqta):
                if arg_xdvx[var_wnki][0] == arg_xdvx[var_egyk][0] or arg_xdvx[
                    var_wnki][1] == arg_xdvx[var_egyk][1]:
                    var_wrnh[var_wnki].append(var_egyk)
                    var_wrnh[var_egyk].append(var_wnki)
        var_dcmd = 0
        var_llti = [False] * var_hqta

        def func_zbxo(arg_rdmc):
            var_llti[arg_rdmc] = True
            for var_rjut in var_wrnh[arg_rdmc]:
                if not var_llti[var_rjut]:
                    func_zbxo(var_rjut)
        for var_wnki in var_ayzf(var_hqta):
            if not var_llti[var_wnki]:
                func_zbxo(var_wnki)
                var_dcmd += 1
        return var_hqta - var_dcmd
