class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:

        def func_hqta(arg_rgwu):
            var_wrnh = var_osiz()
            for var_ayzf in arg_xdvx[arg_rgwu:]:
                if var_ayzf in var_wrnh:
                    return False
                var_wrnh.add(var_ayzf)
            return True
        var_wnki = 0
        for var_egyk in var_dcmd(0, var_llti(arg_xdvx), 3):
            if func_hqta(var_egyk):
                return var_wnki
            var_wnki += 1
        return var_wnki
