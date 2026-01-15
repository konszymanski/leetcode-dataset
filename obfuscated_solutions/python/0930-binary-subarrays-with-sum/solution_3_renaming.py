class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = 0
        var_ayzf = 0
        for var_wnki, var_egyk in var_dcmd(arg_xdvx):
            var_osiz += var_egyk
            while var_rgwu < var_wnki and (arg_xdvx[var_rgwu] == 0 or 
                var_osiz > arg_rcsn):
                if arg_xdvx[var_rgwu] == 1:
                    var_wrnh = 0
                else:
                    var_wrnh += 1
                var_osiz -= arg_xdvx[var_rgwu]
                var_rgwu += 1
            if var_osiz == arg_rcsn:
                var_ayzf += 1 + var_wrnh
        return var_ayzf
