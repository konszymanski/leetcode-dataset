class Solution:

    def func_udax(arg_ihhe, arg_xdvx):

        def func_rcsn(arg_xdvx, arg_bacg, arg_hqta):
            if arg_bacg >= var_rgwu(arg_xdvx):
                return False
            return arg_hqta == 1 or arg_xdvx[arg_bacg] != '0' and (arg_hqta <
                3 or var_wrnh(arg_xdvx[arg_bacg:arg_bacg + arg_hqta]) <= 255)
        var_osiz = []
        arg_hqta = var_rgwu(arg_xdvx)
        for var_ayzf in var_wnki(var_egyk(1, arg_hqta - 9), var_dcmd(4, 
            arg_hqta - 2) + 1):
            if not func_rcsn(arg_xdvx, 0, var_ayzf):
                continue
            for var_llti in var_wnki(var_egyk(1, arg_hqta - var_ayzf - 6), 
                var_dcmd(4, arg_hqta - var_ayzf - 1) + 1):
                if not func_rcsn(arg_xdvx, var_ayzf, var_llti):
                    continue
                for var_zbxo in var_wnki(var_egyk(1, arg_hqta - var_ayzf -
                    var_llti - 3), var_dcmd(4, arg_hqta - var_ayzf -
                    var_llti) + 1):
                    if func_rcsn(arg_xdvx, var_ayzf + var_llti, var_zbxo
                        ) and func_rcsn(arg_xdvx, var_ayzf + var_llti +
                        var_zbxo, arg_hqta - var_ayzf - var_llti - var_zbxo):
                        var_osiz.append(arg_xdvx[:var_ayzf] + '.' +
                            arg_xdvx[var_ayzf:var_ayzf + var_llti] + '.' +
                            arg_xdvx[var_ayzf + var_llti:var_ayzf +
                            var_llti + var_zbxo] + '.' + arg_xdvx[var_ayzf +
                            var_llti + var_zbxo:])
        return var_osiz
