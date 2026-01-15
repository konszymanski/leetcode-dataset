class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu) ->var_rgwu:
        if arg_rcsn < arg_bacg:
            arg_xdvx = arg_xdvx[::-1]
            arg_rcsn, arg_bacg = arg_bacg, arg_rcsn
        var_wrnh, var_osiz, var_ayzf = 0, 0, 0
        for var_wnki in var_egyk(var_dcmd(arg_xdvx)):
            if arg_xdvx[var_wnki] == 'a':
                var_wrnh += 1
            elif arg_xdvx[var_wnki] == 'b':
                if var_wrnh > 0:
                    var_wrnh -= 1
                    var_ayzf += arg_rcsn
                else:
                    var_osiz += 1
            else:
                var_ayzf += var_llti(var_osiz, var_wrnh) * arg_bacg
                var_wrnh = var_osiz = 0
        var_ayzf += var_llti(var_osiz, var_wrnh) * arg_bacg
        return var_ayzf
