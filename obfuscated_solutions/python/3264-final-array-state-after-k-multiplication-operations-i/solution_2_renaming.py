class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu):
        var_wrnh = [(var_osiz, var_ayzf) for var_ayzf, var_osiz in var_wnki
            (arg_xdvx)]
        var_egyk(var_wrnh)
        for var_dcmd in var_llti(arg_rcsn):
            var_dcmd, var_ayzf = var_zbxo(var_wrnh)
            arg_xdvx[var_ayzf] *= arg_bacg
            var_rdmc(var_wrnh, (arg_xdvx[var_ayzf], var_ayzf))
        return arg_xdvx
