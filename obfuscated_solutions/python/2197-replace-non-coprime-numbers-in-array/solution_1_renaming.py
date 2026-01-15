class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu()
        for var_wrnh in arg_xdvx:
            while var_hqta:
                var_osiz = var_ayzf.gcd(var_hqta[-1], var_wrnh)
                if var_osiz > 1:
                    var_wrnh = var_hqta[-1] // var_osiz * var_wrnh
                    var_hqta.pop()
                else:
                    break
            var_hqta.append(var_wrnh)
        return var_hqta
