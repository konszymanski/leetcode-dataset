class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            var_wrnh = var_osiz = 0
            var_ayzf = 1
            while var_ayzf * var_ayzf <= var_rgwu:
                if var_rgwu % var_ayzf == 0:
                    var_wrnh += 1
                    var_osiz += var_ayzf
                    if var_ayzf * var_ayzf != var_rgwu:
                        var_wrnh += 1
                        var_osiz += var_rgwu // var_ayzf
                var_ayzf += 1
            if var_wrnh == 4:
                var_hqta += var_osiz
        return var_hqta
