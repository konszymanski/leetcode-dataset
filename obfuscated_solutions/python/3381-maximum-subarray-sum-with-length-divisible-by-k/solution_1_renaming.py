class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        var_ayzf = -var_wnki.maxsize
        var_egyk = [var_wnki.maxsize // 2] * arg_rcsn
        var_egyk[arg_rcsn - 1] = 0
        for var_dcmd in var_llti(var_rgwu):
            var_osiz += arg_xdvx[var_dcmd]
            var_ayzf = var_zbxo(var_ayzf, var_osiz - var_egyk[var_dcmd %
                arg_rcsn])
            var_egyk[var_dcmd % arg_rcsn] = var_rdmc(var_egyk[var_dcmd %
                arg_rcsn], var_osiz)
        return var_ayzf
