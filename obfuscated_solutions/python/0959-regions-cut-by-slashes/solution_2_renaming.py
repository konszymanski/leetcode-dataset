class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_llti:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_hqta * var_hqta * 4
        var_osiz = [-1] * var_wrnh
        var_ayzf = var_wrnh
        for var_wnki in var_egyk(var_hqta):
            for var_dcmd in var_egyk(var_hqta):
                if var_wnki > 0:
                    var_ayzf -= arg_ihhe._union_triangles(var_osiz,
                        arg_ihhe._get_triangle_index(var_hqta, var_wnki - 1,
                        var_dcmd, 2), arg_ihhe._get_triangle_index(var_hqta,
                        var_wnki, var_dcmd, 0))
                if var_dcmd > 0:
                    var_ayzf -= arg_ihhe._union_triangles(var_osiz,
                        arg_ihhe._get_triangle_index(var_hqta, var_wnki, 
                        var_dcmd - 1, 1), arg_ihhe._get_triangle_index(
                        var_hqta, var_wnki, var_dcmd, 3))
                if arg_xdvx[var_wnki][var_dcmd] != '/':
                    var_ayzf -= arg_ihhe._union_triangles(var_osiz,
                        arg_ihhe._get_triangle_index(var_hqta, var_wnki,
                        var_dcmd, 0), arg_ihhe._get_triangle_index(var_hqta,
                        var_wnki, var_dcmd, 1))
                    var_ayzf -= arg_ihhe._union_triangles(var_osiz,
                        arg_ihhe._get_triangle_index(var_hqta, var_wnki,
                        var_dcmd, 2), arg_ihhe._get_triangle_index(var_hqta,
                        var_wnki, var_dcmd, 3))
                if arg_xdvx[var_wnki][var_dcmd] != '\\':
                    var_ayzf -= arg_ihhe._union_triangles(var_osiz,
                        arg_ihhe._get_triangle_index(var_hqta, var_wnki,
                        var_dcmd, 0), arg_ihhe._get_triangle_index(var_hqta,
                        var_wnki, var_dcmd, 3))
                    var_ayzf -= arg_ihhe._union_triangles(var_osiz,
                        arg_ihhe._get_triangle_index(var_hqta, var_wnki,
                        var_dcmd, 2), arg_ihhe._get_triangle_index(var_hqta,
                        var_wnki, var_dcmd, 1))
        return var_ayzf

    def func_zbxo(arg_ihhe, var_hqta, var_wnki, var_dcmd, arg_rdmc):
        return (var_hqta * var_wnki + var_dcmd) * 4 + arg_rdmc

    def func_rjut(arg_ihhe, var_osiz, arg_lsgw, arg_cbvh):
        var_yjch = arg_ihhe._find_parent(var_osiz, arg_lsgw)
        var_dmio = arg_ihhe._find_parent(var_osiz, arg_cbvh)
        if var_yjch != var_dmio:
            var_osiz[var_yjch] = var_dmio
            return 1
        return 0

    def func_ulfl(arg_ihhe, var_osiz, arg_lsgw):
        if var_osiz[arg_lsgw] == -1:
            return arg_lsgw
        var_osiz[arg_lsgw] = arg_ihhe._find_parent(var_osiz, var_osiz[arg_lsgw]
            )
        return var_osiz[arg_lsgw]
