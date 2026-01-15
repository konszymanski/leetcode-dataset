class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rgwu[var_wrnh]:
        var_bacg = {}
        return arg_ihhe._compute_results(arg_xdvx, var_bacg, 0, var_hqta(
            arg_xdvx) - 1)

    def func_osiz(arg_ihhe, arg_xdvx: var_rcsn, var_bacg: var_egyk,
        arg_ayzf: var_wrnh, arg_wnki: var_wrnh) ->var_rgwu[var_wrnh]:
        if (arg_ayzf, arg_wnki) in var_bacg:
            return var_bacg[arg_ayzf, arg_wnki]
        var_dcmd = []
        if arg_ayzf == arg_wnki:
            var_dcmd.append(var_wrnh(arg_xdvx[arg_ayzf]))
            return var_dcmd
        if arg_wnki - arg_ayzf == 1 and arg_xdvx[arg_ayzf].isdigit():
            var_dcmd.append(var_wrnh(arg_xdvx[arg_ayzf:arg_wnki + 1]))
            return var_dcmd
        for var_llti in var_zbxo(arg_ayzf, arg_wnki + 1):
            if arg_xdvx[var_llti].isdigit():
                continue
            var_rdmc = arg_ihhe._compute_results(arg_xdvx, var_bacg,
                arg_ayzf, var_llti - 1)
            var_rjut = arg_ihhe._compute_results(arg_xdvx, var_bacg, 
                var_llti + 1, arg_wnki)
            for var_lsgw in var_rdmc:
                for var_cbvh in var_rjut:
                    if arg_xdvx[var_llti] == '+':
                        var_dcmd.append(var_lsgw + var_cbvh)
                    elif arg_xdvx[var_llti] == '-':
                        var_dcmd.append(var_lsgw - var_cbvh)
                    elif arg_xdvx[var_llti] == '*':
                        var_dcmd.append(var_lsgw * var_cbvh)
        var_bacg[arg_ayzf, arg_wnki] = var_dcmd
        return var_dcmd
