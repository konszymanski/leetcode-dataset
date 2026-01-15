class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        if not arg_xdvx:
            return ''
        var_hqta = var_rgwu(var_wrnh(var_osiz) for var_osiz in arg_xdvx)
        var_ayzf, var_wnki = 1, var_hqta
        while var_ayzf <= var_wnki:
            var_egyk = (var_ayzf + var_wnki) // 2
            if arg_ihhe.isCommonPrefix(arg_xdvx, var_egyk):
                var_ayzf = var_egyk + 1
            else:
                var_wnki = var_egyk - 1
        return arg_xdvx[0][:(var_ayzf + var_wnki) // 2]

    def func_dcmd(arg_ihhe, arg_xdvx, arg_llti):
        var_zbxo = arg_xdvx[0][:arg_llti]
        for var_rdmc in var_rjut(1, var_wrnh(arg_xdvx)):
            if not arg_xdvx[var_rdmc].startswith(var_zbxo):
                return False
        return True
