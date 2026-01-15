class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = var_rgwu()
        for var_wrnh in var_osiz(var_rcsn):
            if not var_hqta or arg_xdvx[var_wrnh] > var_hqta[-1]:
                var_hqta.append(arg_xdvx[var_wrnh])
            else:
                var_ayzf = var_hqta[-1]
                while var_hqta and arg_xdvx[var_wrnh] < var_hqta[-1]:
                    var_hqta.pop()
                var_hqta.append(var_ayzf)
        return var_bacg(var_hqta)
