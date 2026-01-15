class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):

        def func_bacg(arg_hqta):
            if not arg_hqta:
                return 0, 0, var_rgwu('inf')
            var_wrnh = func_bacg(arg_hqta.left)
            var_osiz = func_bacg(arg_hqta.right)
            var_ayzf = var_wrnh[1] + var_osiz[1]
            var_wnki = var_egyk(var_wrnh[2] + var_egyk(var_osiz[1:]), 
                var_osiz[2] + var_egyk(var_wrnh[1:]))
            var_dcmd = 1 + var_egyk(var_wrnh) + var_egyk(var_osiz)
            return var_ayzf, var_wnki, var_dcmd
        return var_egyk(func_bacg(arg_rcsn)[1:])
