class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_rcsn
        [var_bacg]]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = []
        for var_osiz in var_ayzf(2 ** var_hqta, 2 ** (var_hqta + 1)):
            var_wnki = var_egyk(var_osiz)[3:]
            var_wrnh.append([arg_xdvx[var_dcmd] for var_dcmd in var_ayzf(
                var_hqta) if var_wnki[var_dcmd] == '1'])
        return var_wrnh
