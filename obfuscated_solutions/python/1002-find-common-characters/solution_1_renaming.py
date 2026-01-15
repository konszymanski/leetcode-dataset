class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = []
        var_osiz = var_ayzf.Counter(arg_xdvx[0])
        for var_wnki in var_egyk(1, var_hqta):
            var_dcmd = var_ayzf.Counter(arg_xdvx[var_wnki])
            for var_llti in var_osiz.keys():
                var_osiz[var_llti] = var_zbxo(var_osiz[var_llti], var_dcmd[
                    var_llti])
        for var_llti, var_rdmc in var_osiz.items():
            for var_rjut in var_egyk(var_rdmc):
                var_wrnh.append(var_llti)
        return var_wrnh
