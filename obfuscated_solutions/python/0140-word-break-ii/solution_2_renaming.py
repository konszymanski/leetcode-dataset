class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_hqta[var_bacg]:
        var_rgwu = var_wrnh(arg_rcsn)
        var_osiz = {}
        return arg_ihhe._dfs(arg_xdvx, var_rgwu, var_osiz)

    def func_ayzf(arg_ihhe, arg_wnki: var_bacg, var_rgwu: var_wrnh,
        var_osiz: var_egyk) ->var_hqta[var_bacg]:
        if arg_wnki in var_osiz:
            return var_osiz[arg_wnki]
        if not arg_wnki:
            return ['']
        var_dcmd = []
        for var_llti in var_zbxo(1, var_rdmc(arg_wnki) + 1):
            var_rjut = arg_wnki[:var_llti]
            if var_rjut in var_rgwu:
                for var_lsgw in arg_ihhe._dfs(arg_wnki[var_llti:], var_rgwu,
                    var_osiz):
                    var_dcmd.append(var_rjut + (' ' if var_lsgw else '') +
                        var_lsgw)
        var_osiz[arg_wnki] = var_dcmd
        return var_dcmd
