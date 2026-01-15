class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_wnki[
        var_bacg]:
        var_hqta = [0] * arg_xdvx
        var_rgwu = 0
        for var_wrnh in var_osiz(1, arg_xdvx - arg_rcsn):
            var_hqta[var_rgwu] = var_wrnh
            var_rgwu += 1
        for var_ayzf in var_osiz(arg_rcsn + 1):
            var_hqta[var_rgwu] = (arg_xdvx - arg_rcsn + var_ayzf // 2 if 
                var_ayzf % 2 == 0 else arg_xdvx - var_ayzf // 2)
            var_rgwu += 1
        return var_hqta
