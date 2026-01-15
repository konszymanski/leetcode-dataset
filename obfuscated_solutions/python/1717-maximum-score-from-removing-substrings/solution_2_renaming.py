class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = 0
        arg_xdvx = var_osiz(arg_xdvx)
        if arg_rcsn > arg_bacg:
            var_wrnh += arg_ihhe.remove_substring(arg_xdvx, 'ab', arg_rcsn)
            var_wrnh += arg_ihhe.remove_substring(arg_xdvx, 'ba', arg_bacg)
        else:
            var_wrnh += arg_ihhe.remove_substring(arg_xdvx, 'ba', arg_bacg)
            var_wrnh += arg_ihhe.remove_substring(arg_xdvx, 'ab', arg_rcsn)
        return var_wrnh

    def func_ayzf(arg_ihhe, arg_wnki, arg_egyk, arg_dcmd):
        var_wrnh = 0
        var_llti = 0
        for var_zbxo in var_rdmc(0, var_rjut(arg_wnki)):
            arg_wnki[var_llti] = arg_wnki[var_zbxo]
            var_llti += 1
            if var_llti > 1 and arg_wnki[var_llti - 2] == arg_egyk[0
                ] and arg_wnki[var_llti - 1] == arg_egyk[1]:
                var_llti -= 2
                var_wrnh += arg_dcmd
        del arg_wnki[var_llti:]
        return var_wrnh
