class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rdmc[var_llti]:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [0] * var_bacg
        var_wrnh = 0
        var_osiz = 0
        var_ayzf = 0
        var_wnki = 0
        for var_egyk in var_dcmd(var_bacg):
            var_rgwu[var_egyk] += var_osiz
            var_wrnh += var_llti(arg_xdvx[var_egyk])
            var_osiz += var_wrnh
            var_zbxo = var_bacg - 1 - var_egyk
            var_rgwu[var_zbxo] += var_wnki
            var_ayzf += var_llti(arg_xdvx[var_zbxo])
            var_wnki += var_ayzf
        return var_rgwu
