class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = 1
        var_hqta = var_rgwu(arg_xdvx)
        while var_bacg < var_hqta:
            var_wrnh = (var_bacg + var_hqta) // 2
            if arg_ihhe._is_possible(var_wrnh, arg_xdvx, arg_rcsn):
                var_hqta = var_wrnh
            else:
                var_bacg = var_wrnh + 1
        return var_bacg

    def func_osiz(arg_ihhe, arg_ayzf, arg_xdvx, arg_rcsn):
        var_wnki = 0
        for var_egyk in arg_xdvx:
            var_dcmd = var_llti.ceil(var_egyk / arg_ayzf) - 1
            var_wnki += var_dcmd
            if var_wnki > arg_rcsn:
                return False
        return True
