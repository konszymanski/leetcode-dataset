class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_dmio:
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_osiz(arg_rcsn)
        var_ayzf = var_rgwu + var_wrnh

        def func_wnki(arg_egyk, arg_dcmd, arg_llti, arg_zbxo, arg_rdmc):
            if arg_dcmd > arg_llti:
                return arg_rcsn[arg_egyk - arg_dcmd]
            if arg_zbxo > arg_rdmc:
                return arg_xdvx[arg_egyk - arg_zbxo]
            var_rjut, var_lsgw = (arg_dcmd + arg_llti) // 2, (arg_zbxo +
                arg_rdmc) // 2
            var_cbvh, var_yjch = arg_xdvx[var_rjut], arg_rcsn[var_lsgw]
            if var_rjut + var_lsgw < arg_egyk:
                if var_cbvh > var_yjch:
                    return func_wnki(arg_egyk, arg_dcmd, arg_llti, var_lsgw +
                        1, arg_rdmc)
                else:
                    return func_wnki(arg_egyk, var_rjut + 1, arg_llti,
                        arg_zbxo, arg_rdmc)
            elif var_cbvh > var_yjch:
                return func_wnki(arg_egyk, arg_dcmd, var_rjut - 1, arg_zbxo,
                    arg_rdmc)
            else:
                return func_wnki(arg_egyk, arg_dcmd, arg_llti, arg_zbxo, 
                    var_lsgw - 1)
        if var_ayzf % 2:
            return func_wnki(var_ayzf // 2, 0, var_rgwu - 1, 0, var_wrnh - 1)
        else:
            return (func_wnki(var_ayzf // 2 - 1, 0, var_rgwu - 1, 0, 
                var_wrnh - 1) + func_wnki(var_ayzf // 2, 0, var_rgwu - 1, 0,
                var_wrnh - 1)) / 2
