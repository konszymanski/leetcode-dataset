class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        var_osiz = [([-1] * 4) for var_ayzf in var_wnki(var_hqta)]
        var_egyk = [([-1] * 4) for var_ayzf in var_wnki(var_hqta)]
        for var_dcmd in var_wnki(var_hqta):
            var_wrnh += arg_ihhe._count_increasing_teams(arg_xdvx, var_dcmd,
                1, var_osiz) + arg_ihhe._count_decreasing_teams(arg_xdvx,
                var_dcmd, 1, var_egyk)
        return var_wrnh

    def func_llti(arg_ihhe, arg_xdvx: var_rcsn[var_bacg], arg_zbxo:
        var_bacg, arg_rdmc: var_bacg, var_osiz: var_rcsn[var_rcsn[var_bacg]]
        ) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        if arg_zbxo == var_hqta:
            return 0
        if arg_rdmc == 3:
            return 1
        if var_osiz[arg_zbxo][arg_rdmc] != -1:
            return var_osiz[arg_zbxo][arg_rdmc]
        var_rjut = 0
        for var_lsgw in var_wnki(arg_zbxo + 1, var_hqta):
            if arg_xdvx[var_lsgw] > arg_xdvx[arg_zbxo]:
                var_rjut += arg_ihhe._count_increasing_teams(arg_xdvx,
                    var_lsgw, arg_rdmc + 1, var_osiz)
        var_osiz[arg_zbxo][arg_rdmc] = var_rjut
        return var_rjut

    def func_cbvh(arg_ihhe, arg_xdvx: var_rcsn[var_bacg], arg_zbxo:
        var_bacg, arg_rdmc: var_bacg, var_egyk: var_rcsn[var_rcsn[var_bacg]]
        ) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        if arg_zbxo == var_hqta:
            return 0
        if arg_rdmc == 3:
            return 1
        if var_egyk[arg_zbxo][arg_rdmc] != -1:
            return var_egyk[arg_zbxo][arg_rdmc]
        var_rjut = 0
        for var_lsgw in var_wnki(arg_zbxo + 1, var_hqta):
            if arg_xdvx[var_lsgw] < arg_xdvx[arg_zbxo]:
                var_rjut += arg_ihhe._count_decreasing_teams(arg_xdvx,
                    var_lsgw, arg_rdmc + 1, var_egyk)
        var_egyk[arg_zbxo][arg_rdmc] = var_rjut
        return var_rjut
