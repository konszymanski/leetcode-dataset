class Graph:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        arg_ihhe.adj_matrix = [([var_bacg] * arg_xdvx) for var_hqta in
            var_rgwu(arg_xdvx)]
        for var_wrnh, var_osiz, var_ayzf in arg_rcsn:
            arg_ihhe.adj_matrix[var_wrnh][var_osiz] = var_ayzf
        for var_wnki in var_rgwu(arg_xdvx):
            arg_ihhe.adj_matrix[var_wnki][var_wnki] = 0
        for var_wnki in var_rgwu(arg_xdvx):
            for var_egyk in var_rgwu(arg_xdvx):
                for var_dcmd in var_rgwu(arg_xdvx):
                    arg_ihhe.adj_matrix[var_egyk][var_dcmd] = var_llti(arg_ihhe
                        .adj_matrix[var_egyk][var_dcmd], arg_ihhe.
                        adj_matrix[var_egyk][var_wnki] + arg_ihhe.
                        adj_matrix[var_wnki][var_dcmd])

    def func_zbxo(arg_ihhe, arg_rdmc: var_rjut[var_lsgw]) ->None:
        var_wrnh, var_osiz, var_ayzf = arg_rdmc
        arg_xdvx = var_cbvh(arg_ihhe.adj_matrix)
        for var_wnki in var_rgwu(arg_xdvx):
            for var_egyk in var_rgwu(arg_xdvx):
                arg_ihhe.adj_matrix[var_wnki][var_egyk] = var_llti(arg_ihhe
                    .adj_matrix[var_wnki][var_egyk], arg_ihhe.adj_matrix[
                    var_wnki][var_wrnh] + arg_ihhe.adj_matrix[var_osiz][
                    var_egyk] + var_ayzf)

    def func_yjch(arg_ihhe, arg_dmio, arg_ulfl):
        if arg_ihhe.adj_matrix[arg_dmio][arg_ulfl] == var_bacg:
            return -1
        return arg_ihhe.adj_matrix[arg_dmio][arg_ulfl]
