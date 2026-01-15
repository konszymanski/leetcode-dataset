class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_osiz:
        arg_ihhe._quick_sort(arg_xdvx, 0, var_hqta(arg_xdvx) - 1)
        var_rgwu = ''.join(var_wrnh(var_osiz, arg_xdvx))
        return '0' if var_rgwu[0] == '0' else var_rgwu

    def func_ayzf(arg_ihhe, arg_xdvx: var_rcsn[var_bacg], arg_wnki:
        var_bacg, arg_egyk: var_bacg) ->None:
        if arg_wnki >= arg_egyk:
            return
        var_dcmd = arg_ihhe._partition(arg_xdvx, arg_wnki, arg_egyk)
        arg_ihhe._quick_sort(arg_xdvx, arg_wnki, var_dcmd - 1)
        arg_ihhe._quick_sort(arg_xdvx, var_dcmd + 1, arg_egyk)

    def func_llti(arg_ihhe, arg_xdvx: var_rcsn[var_bacg], arg_wnki:
        var_bacg, arg_egyk: var_bacg) ->var_bacg:
        var_zbxo = arg_xdvx[arg_egyk]
        var_rdmc = arg_wnki
        for var_rjut in var_lsgw(arg_wnki, arg_egyk):
            if arg_ihhe._compare(arg_xdvx[var_rjut], var_zbxo):
                arg_xdvx[var_rjut], arg_xdvx[var_rdmc] = arg_xdvx[var_rdmc
                    ], arg_xdvx[var_rjut]
                var_rdmc += 1
        arg_xdvx[var_rdmc], arg_xdvx[arg_egyk] = arg_xdvx[arg_egyk], arg_xdvx[
            var_rdmc]
        return var_rdmc

    def func_cbvh(arg_ihhe, arg_yjch: var_bacg, arg_dmio: var_bacg) ->var_ulfl:
        return var_osiz(arg_yjch) + var_osiz(arg_dmio) > var_osiz(arg_dmio
            ) + var_osiz(arg_yjch)
