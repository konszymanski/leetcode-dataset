class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_wrnh[var_osiz
        ], arg_bacg: var_ayzf, arg_hqta: var_ayzf) ->var_osiz:
        arg_rcsn[arg_bacg] = True
        if arg_bacg == arg_hqta:
            return True
        for var_wnki in arg_xdvx.get(arg_bacg, []):
            if not arg_rcsn[var_wnki]:
                if arg_ihhe.isPrerequisite(arg_xdvx, arg_rcsn, var_wnki,
                    arg_hqta):
                    return True
        return False

    def func_egyk(arg_ihhe, arg_dcmd: var_ayzf, arg_llti: var_wrnh[var_wrnh
        [var_ayzf]], arg_zbxo: var_wrnh[var_wrnh[var_ayzf]]) ->var_wrnh[
        var_osiz]:
        arg_xdvx = {var_rdmc: [] for var_rdmc in var_rjut(arg_dcmd)}
        for var_lsgw in arg_llti:
            arg_xdvx[var_lsgw[0]].append(var_lsgw[1])
        var_cbvh = []
        for var_yjch in arg_zbxo:
            arg_rcsn = [False] * arg_dcmd
            var_cbvh.append(arg_ihhe.isPrerequisite(arg_xdvx, arg_rcsn,
                var_yjch[0], var_yjch[1]))
        return var_cbvh
