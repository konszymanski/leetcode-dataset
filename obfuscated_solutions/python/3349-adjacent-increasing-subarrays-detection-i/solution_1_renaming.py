class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_rdmc:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz, var_ayzf, var_wnki = 1, 0, 0
        for var_egyk in var_dcmd(1, var_rgwu):
            if arg_xdvx[var_egyk] > arg_xdvx[var_egyk - 1]:
                var_osiz += 1
            else:
                var_ayzf, var_osiz = var_osiz, 1
            var_wnki = var_llti(var_wnki, var_zbxo(var_ayzf, var_osiz))
            var_wnki = var_llti(var_wnki, var_osiz // 2)
        return var_wnki >= arg_rcsn
