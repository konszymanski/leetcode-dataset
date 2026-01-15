class Helper:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.x = arg_xdvx
        arg_ihhe.result = 0
        arg_ihhe.large = var_rcsn()
        arg_ihhe.small = var_rcsn()
        arg_ihhe.occ = var_bacg(var_hqta)

    def func_rgwu(arg_ihhe, arg_wrnh):
        if arg_ihhe.occ[arg_wrnh] > 0:
            arg_ihhe.internal_remove((arg_ihhe.occ[arg_wrnh], arg_wrnh))
        arg_ihhe.occ[arg_wrnh] += 1
        arg_ihhe.internal_insert((arg_ihhe.occ[arg_wrnh], arg_wrnh))

    def func_osiz(arg_ihhe, arg_wrnh):
        arg_ihhe.internal_remove((arg_ihhe.occ[arg_wrnh], arg_wrnh))
        arg_ihhe.occ[arg_wrnh] -= 1
        if arg_ihhe.occ[arg_wrnh] > 0:
            arg_ihhe.internal_insert((arg_ihhe.occ[arg_wrnh], arg_wrnh))

    def func_ayzf(arg_ihhe):
        return arg_ihhe.result

    def func_wnki(arg_ihhe, arg_egyk):
        if var_dcmd(arg_ihhe.large) < arg_ihhe.x or arg_egyk > arg_ihhe.large[0
            ]:
            arg_ihhe.result += arg_egyk[0] * arg_egyk[1]
            arg_ihhe.large.add(arg_egyk)
            if var_dcmd(arg_ihhe.large) > arg_ihhe.x:
                var_llti = arg_ihhe.large[0]
                arg_ihhe.result -= var_llti[0] * var_llti[1]
                arg_ihhe.large.remove(var_llti)
                arg_ihhe.small.add(var_llti)
        else:
            arg_ihhe.small.add(arg_egyk)

    def func_zbxo(arg_ihhe, arg_egyk):
        if arg_egyk >= arg_ihhe.large[0]:
            arg_ihhe.result -= arg_egyk[0] * arg_egyk[1]
            arg_ihhe.large.remove(arg_egyk)
            if arg_ihhe.small:
                var_rdmc = arg_ihhe.small[-1]
                arg_ihhe.result += var_rdmc[0] * var_rdmc[1]
                arg_ihhe.small.remove(var_rdmc)
                arg_ihhe.large.add(var_rdmc)
        else:
            arg_ihhe.small.remove(arg_egyk)


class Solution:

    def func_rjut(arg_ihhe, arg_lsgw, arg_cbvh, arg_xdvx):
        var_yjch = var_dmio(arg_xdvx)
        var_ulfl = []
        for var_lgvi in var_wvuc(var_dcmd(arg_lsgw)):
            var_yjch.insert(arg_lsgw[var_lgvi])
            if var_lgvi >= arg_cbvh:
                var_yjch.remove(arg_lsgw[var_lgvi - arg_cbvh])
            if var_lgvi >= arg_cbvh - 1:
                var_ulfl.append(var_yjch.get())
        return var_ulfl
