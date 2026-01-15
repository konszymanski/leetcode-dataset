class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = [0, 0, 1, -1]
        var_bacg = [1, -1, 0, 0]
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = [[(-1) for var_ayzf in var_wnki(var_wrnh)] for var_ayzf in
            var_wnki(var_hqta)]
        var_egyk = var_dcmd()
        for var_llti in var_wnki(var_hqta):
            for var_zbxo in var_wnki(var_wrnh):
                if arg_xdvx[var_llti][var_zbxo] == 1:
                    var_egyk.append((var_llti, var_zbxo))
                    var_osiz[var_llti][var_zbxo] = 0
        var_rdmc = 1
        while var_egyk:
            var_rjut = var_rgwu(var_egyk)
            for var_ayzf in var_wnki(var_rjut):
                var_lsgw = var_egyk.popleft()
                for var_cbvh in var_wnki(4):
                    var_yjch = var_lsgw[0] + var_rcsn[var_cbvh]
                    var_dmio = var_lsgw[1] + var_bacg[var_cbvh]
                    if arg_ihhe._is_valid_cell(var_yjch, var_dmio, var_hqta,
                        var_wrnh) and var_osiz[var_yjch][var_dmio] == -1:
                        var_osiz[var_yjch][var_dmio] = var_rdmc
                        var_egyk.append((var_yjch, var_dmio))
            var_rdmc += 1
        return var_osiz

    def func_ulfl(arg_ihhe, var_llti, var_zbxo, var_hqta, var_wrnh):
        """Check if a cell is within the grid boundaries."""
        return 0 <= var_llti < var_hqta and 0 <= var_zbxo < var_wrnh
