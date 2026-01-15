class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg, var_hqta = 1, var_rgwu(arg_xdvx)
        var_wrnh = var_osiz(arg_xdvx)
        while var_bacg < var_hqta:
            var_ayzf = (var_bacg + var_hqta) // 2
            var_wnki = 0
            var_egyk = 0
            while var_egyk < var_wrnh:
                if arg_xdvx[var_egyk] <= var_ayzf:
                    var_wnki += 1
                    var_egyk += 2
                else:
                    var_egyk += 1
            if var_wnki >= arg_rcsn:
                var_hqta = var_ayzf
            else:
                var_bacg = var_ayzf + 1
        return var_bacg
