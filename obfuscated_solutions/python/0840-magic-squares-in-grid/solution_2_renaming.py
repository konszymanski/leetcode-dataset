class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_wrnh(arg_xdvx[0])
        for var_ayzf in var_wnki(var_rgwu - 2):
            for var_egyk in var_wnki(var_osiz - 2):
                if arg_ihhe._isMagicSquare(arg_xdvx, var_ayzf, var_egyk):
                    var_hqta += 1
        return var_hqta

    def func_dcmd(arg_ihhe, arg_xdvx, var_ayzf, var_egyk):
        var_llti = '2943816729438167'
        var_zbxo = '7618349276183492'
        var_rdmc = []
        var_rjut = [0, 1, 2, 5, 8, 7, 6, 3]
        for var_lsgw in var_rjut:
            var_cbvh = arg_xdvx[var_ayzf + var_lsgw // 3][var_egyk + 
                var_lsgw % 3]
            var_rdmc.append(var_yjch(var_cbvh))
        var_dmio = ''.join(var_rdmc)
        return arg_xdvx[var_ayzf][var_egyk] % 2 == 0 and (var_llti.find(
            var_dmio) != -1 or var_zbxo.find(var_dmio) != -1) and arg_xdvx[
            var_ayzf + 1][var_egyk + 1] == 5
