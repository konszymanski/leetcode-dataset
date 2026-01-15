class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_zbxo[var_rdmc[var_llti]]:
        var_bacg = [[] for var_hqta in var_rgwu(arg_xdvx + 1)]
        var_bacg[0].append(None)
        for var_wrnh in var_rgwu(1, arg_xdvx + 1):
            for var_osiz in var_rgwu(1, var_wrnh + 1):
                var_ayzf = var_wrnh - var_osiz
                for var_wnki in var_bacg[var_osiz - 1]:
                    for var_egyk in var_bacg[var_ayzf]:
                        var_dcmd = var_llti(var_osiz, var_wnki, arg_ihhe.
                            clone(var_egyk, var_osiz))
                        var_bacg[var_wrnh].append(var_dcmd)
        return var_bacg[arg_xdvx]

    def func_rjut(arg_ihhe, arg_lsgw: var_rdmc[var_llti], arg_cbvh: var_rcsn
        ) ->var_rdmc[var_llti]:
        if not arg_lsgw:
            return None
        var_yjch = var_llti(arg_lsgw.val + arg_cbvh)
        var_yjch.left = arg_ihhe.clone(arg_lsgw.left, arg_cbvh)
        var_yjch.right = arg_ihhe.clone(arg_lsgw.right, arg_cbvh)
        return var_yjch
