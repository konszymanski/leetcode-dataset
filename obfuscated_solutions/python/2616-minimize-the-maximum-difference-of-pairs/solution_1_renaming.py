class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        arg_xdvx.sort()
        var_rgwu = var_wrnh(arg_xdvx)

        def func_osiz(arg_ayzf):
            var_wnki, var_egyk = 0, 0
            while var_wnki < var_rgwu - 1:
                if arg_xdvx[var_wnki + 1] - arg_xdvx[var_wnki] <= arg_ayzf:
                    var_egyk += 1
                    var_wnki += 1
                var_wnki += 1
            return var_egyk
        var_dcmd, var_llti = 0, arg_xdvx[-1] - arg_xdvx[0]
        while var_dcmd < var_llti:
            var_zbxo = var_dcmd + (var_llti - var_dcmd) // 2
            if func_osiz(var_zbxo) >= arg_rcsn:
                var_llti = var_zbxo
            else:
                var_dcmd = var_zbxo + 1
        return var_dcmd
