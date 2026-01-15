class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = []
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            var_ayzf = arg_ihhe._compute_lps_array(arg_xdvx[var_rgwu])
            for var_wnki in var_wrnh(var_osiz(arg_xdvx)):
                if var_rgwu == var_wnki:
                    continue
                if arg_ihhe._is_substring_of(arg_xdvx[var_rgwu], arg_xdvx[
                    var_wnki], var_ayzf):
                    var_hqta.append(arg_xdvx[var_rgwu])
                    break
        return var_hqta

    def func_egyk(arg_ihhe, arg_dcmd: var_bacg) ->var_rcsn[var_rdmc]:
        var_ayzf = [0] * var_osiz(arg_dcmd)
        var_llti = 1
        var_zbxo = 0
        while var_llti < var_osiz(arg_dcmd):
            if arg_dcmd[var_llti] == arg_dcmd[var_zbxo]:
                var_zbxo += 1
                var_ayzf[var_llti] = var_zbxo
                var_llti += 1
            elif var_zbxo > 0:
                var_zbxo = var_ayzf[var_zbxo - 1]
            else:
                var_llti += 1
        return var_ayzf

    def func_rjut(arg_ihhe, arg_dcmd: var_bacg, arg_lsgw: var_bacg, var_ayzf
        ) ->var_dmio:
        var_cbvh = 0
        var_yjch = 0
        while var_cbvh < var_osiz(arg_lsgw):
            if arg_lsgw[var_cbvh] == arg_dcmd[var_yjch]:
                var_cbvh += 1
                var_yjch += 1
                if var_yjch == var_osiz(arg_dcmd):
                    return True
            elif var_yjch > 0:
                var_yjch = var_ayzf[var_yjch - 1]
            else:
                var_cbvh += 1
        return False
