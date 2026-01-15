class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        if arg_xdvx < 2:
            return False
        if arg_xdvx == 2 or arg_xdvx == 3:
            return True
        if arg_xdvx % 2 == 0:
            return False
        var_rcsn = 3
        while var_rcsn * var_rcsn <= arg_xdvx:
            if arg_xdvx % var_rcsn == 0:
                return False
            var_rcsn += 2
        return True

    def func_bacg(arg_ihhe, arg_hqta, arg_rgwu):
        if arg_hqta <= 2 and arg_rgwu >= 3:
            return [2, 3]
        var_wrnh = -1
        var_osiz = -1
        var_ayzf = -1
        var_wnki = var_egyk('inf')
        for var_dcmd in var_llti(arg_hqta, arg_rgwu + 1):
            if arg_ihhe.isPrime(var_dcmd):
                if var_wrnh != -1:
                    var_zbxo = var_dcmd - var_wrnh
                    if var_zbxo < var_wnki:
                        var_wnki = var_zbxo
                        var_osiz = var_wrnh
                        var_ayzf = var_dcmd
                    if var_zbxo == 2:
                        return [var_wrnh, var_dcmd]
                var_wrnh = var_dcmd
        return [var_osiz, var_ayzf]
