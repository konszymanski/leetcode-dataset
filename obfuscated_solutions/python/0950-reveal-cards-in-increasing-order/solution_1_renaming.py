class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [0] * var_hqta
        var_osiz = False
        var_ayzf = 0
        var_wnki = 0
        arg_xdvx.sort()
        while var_ayzf < var_hqta:
            if var_wrnh[var_wnki] == 0:
                if not var_osiz:
                    var_wrnh[var_wnki] = arg_xdvx[var_ayzf]
                    var_ayzf += 1
                var_osiz = not var_osiz
            var_wnki = (var_wnki + 1) % var_hqta
        return var_wrnh
