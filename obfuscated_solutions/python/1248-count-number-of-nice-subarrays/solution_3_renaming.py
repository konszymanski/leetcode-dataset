class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = 0
        var_ayzf = 0
        for var_wnki in var_egyk(var_dcmd(arg_xdvx)):
            if arg_xdvx[var_wnki] % 2 == 1:
                var_osiz += 1
            if var_osiz == arg_rcsn:
                var_wrnh = 0
                while var_osiz == arg_rcsn:
                    var_osiz -= arg_xdvx[var_ayzf] % 2
                    var_wrnh += 1
                    var_ayzf += 1
            var_rgwu += var_wrnh
        return var_rgwu
