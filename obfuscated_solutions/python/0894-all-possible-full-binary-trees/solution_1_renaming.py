class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_llti[var_bacg]:
        if arg_xdvx % 2 == 0:
            return []
        if arg_xdvx == 1:
            return [var_bacg()]
        var_hqta = []
        for var_rgwu in var_wrnh(1, arg_xdvx, 2):
            var_osiz = arg_ihhe.allPossibleFBT(var_rgwu)
            var_ayzf = arg_ihhe.allPossibleFBT(arg_xdvx - var_rgwu - 1)
            for var_wnki in var_osiz:
                for var_egyk in var_ayzf:
                    var_dcmd = var_bacg(0, var_wnki, var_egyk)
                    var_hqta.append(var_dcmd)
        return var_hqta
