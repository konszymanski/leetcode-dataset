class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = 0
        for var_hqta in arg_xdvx:
            var_bacg = var_rgwu(var_bacg, var_hqta)
        var_wrnh = 0
        var_osiz = var_bacg
        while var_wrnh < var_osiz:
            var_ayzf = (var_wrnh + var_osiz + 1) // 2
            if arg_ihhe._can_allocate_candies(arg_xdvx, arg_rcsn, var_ayzf):
                var_wrnh = var_ayzf
            else:
                var_osiz = var_ayzf - 1
        return var_wrnh

    def func_wnki(arg_ihhe, arg_xdvx, arg_rcsn, arg_egyk):
        var_dcmd = 0
        for var_llti in arg_xdvx:
            var_dcmd += var_llti // arg_egyk
        return var_dcmd >= arg_rcsn
