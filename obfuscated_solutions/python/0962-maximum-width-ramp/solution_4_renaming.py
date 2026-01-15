class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = []
        for var_rgwu in var_wrnh(var_rcsn):
            if not var_hqta or arg_xdvx[var_hqta[-1]] > arg_xdvx[var_rgwu]:
                var_hqta.append(var_rgwu)
        var_osiz = 0
        for var_ayzf in var_wrnh(var_rcsn - 1, -1, -1):
            while var_hqta and arg_xdvx[var_hqta[-1]] <= arg_xdvx[var_ayzf]:
                var_osiz = var_wnki(var_osiz, var_ayzf - var_hqta[-1])
                var_hqta.pop()
        return var_osiz
