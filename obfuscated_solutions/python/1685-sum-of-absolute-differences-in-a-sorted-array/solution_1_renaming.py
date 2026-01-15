class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [arg_xdvx[0]]
        for var_osiz in var_ayzf(1, var_hqta):
            var_wrnh.append(var_wrnh[-1] + arg_xdvx[var_osiz])
        var_wnki = []
        for var_osiz in var_ayzf(var_rgwu(arg_xdvx)):
            var_egyk = var_wrnh[var_osiz] - arg_xdvx[var_osiz]
            var_dcmd = var_wrnh[-1] - var_wrnh[var_osiz]
            var_llti = var_osiz
            var_zbxo = var_hqta - 1 - var_osiz
            var_rdmc = var_llti * arg_xdvx[var_osiz] - var_egyk
            var_rjut = var_dcmd - var_zbxo * arg_xdvx[var_osiz]
            var_wnki.append(var_rdmc + var_rjut)
        return var_wnki
