class Solution:
    var_udax = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def func_ihhe(arg_xdvx, arg_rcsn):

        def func_bacg(arg_hqta, arg_rgwu):
            return 0 <= arg_hqta < var_wrnh(arg_rcsn
                ) and 0 <= arg_rgwu < var_wrnh(arg_rcsn[0])
        var_osiz, var_ayzf = var_wrnh(arg_rcsn), var_wrnh(arg_rcsn[0])
        var_wnki = [([var_egyk('inf')] * var_ayzf) for var_dcmd in var_llti
            (var_osiz)]
        var_wnki[0][0] = 0
        var_zbxo = var_rdmc([(0, 0, 0)])
        while var_zbxo:
            var_rjut, arg_hqta, arg_rgwu = var_zbxo.popleft()
            for var_lsgw, var_cbvh in arg_xdvx._directions:
                var_yjch, var_dmio = arg_hqta + var_lsgw, arg_rgwu + var_cbvh
                if func_bacg(var_yjch, var_dmio) and var_wnki[var_yjch][
                    var_dmio] == var_egyk('inf'):
                    if arg_rcsn[var_yjch][var_dmio] == 1:
                        var_wnki[var_yjch][var_dmio] = var_rjut + 1
                        var_zbxo.append((var_rjut + 1, var_yjch, var_dmio))
                    else:
                        var_wnki[var_yjch][var_dmio] = var_rjut
                        var_zbxo.appendleft((var_rjut, var_yjch, var_dmio))
        return var_wnki[var_osiz - 1][var_ayzf - 1]
