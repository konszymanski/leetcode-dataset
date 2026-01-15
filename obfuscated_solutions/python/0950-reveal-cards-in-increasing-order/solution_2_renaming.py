class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_osiz()
        for var_ayzf in var_wnki(var_hqta):
            var_wrnh.append(var_ayzf)
        arg_xdvx.sort()
        var_egyk = [0] * var_hqta
        for var_dcmd in arg_xdvx:
            var_egyk[var_wrnh.popleft()] = var_dcmd
            if var_wrnh:
                var_wrnh.append(var_wrnh.popleft())
        return var_egyk
