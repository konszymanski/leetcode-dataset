class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_osiz[var_ayzf]:
        var_rgwu = var_wrnh(arg_xdvx)
        return arg_ihhe._construct_tree(0, var_rgwu - 1, 0, arg_xdvx, arg_rcsn)

    def func_wnki(arg_ihhe, arg_egyk: var_hqta, arg_dcmd: var_hqta,
        arg_llti: var_hqta, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_osiz[var_ayzf]:
        if arg_egyk > arg_dcmd:
            return None
        if arg_egyk == arg_dcmd:
            return var_ayzf(arg_xdvx[arg_egyk])
        var_zbxo = arg_xdvx[arg_egyk + 1]
        var_rdmc = 1
        while arg_rcsn[arg_llti + var_rdmc - 1] != var_zbxo:
            var_rdmc += 1
        var_rjut = var_ayzf(arg_xdvx[arg_egyk])
        var_rjut.left = arg_ihhe._construct_tree(arg_egyk + 1, arg_egyk +
            var_rdmc, arg_llti, arg_xdvx, arg_rcsn)
        var_rjut.right = arg_ihhe._construct_tree(arg_egyk + var_rdmc + 1,
            arg_dcmd, arg_llti + var_rdmc, arg_xdvx, arg_rcsn)
        return var_rjut
