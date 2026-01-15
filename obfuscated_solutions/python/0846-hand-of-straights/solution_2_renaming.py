class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_lsgw:
        var_rgwu = var_wrnh(var_hqta)
        for var_osiz in arg_xdvx:
            var_rgwu[var_osiz] += 1
        var_ayzf = var_wnki(var_rgwu.keys())
        var_egyk = var_dcmd()
        var_llti = -1
        var_zbxo = 0
        for var_rdmc in var_ayzf:
            if var_zbxo > 0 and var_rdmc > var_llti + 1 or var_zbxo > var_rgwu[
                var_rdmc]:
                return False
            var_egyk.append(var_rgwu[var_rdmc] - var_zbxo)
            var_llti = var_rdmc
            var_zbxo = var_rgwu[var_rdmc]
            if var_rjut(var_egyk) == arg_rcsn:
                var_zbxo -= var_egyk.popleft()
        return var_zbxo == 0
