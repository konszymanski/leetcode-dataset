class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        return arg_hqta == 1 or arg_rcsn[arg_bacg] != '0' and (arg_hqta < 3 or
            arg_rcsn[arg_bacg:arg_bacg + arg_hqta] <= '255')

    def func_rgwu(arg_xdvx, arg_rcsn, arg_wrnh, arg_osiz, arg_ayzf):
        var_wnki = var_egyk(arg_rcsn) - arg_wrnh
        var_dcmd = 4 - var_egyk(arg_osiz)
        if var_wnki > var_dcmd * 3 or var_wnki < var_dcmd:
            return
        if var_egyk(arg_osiz) == 3:
            if arg_xdvx.valid(arg_rcsn, arg_wrnh, var_wnki):
                var_llti = ''
                var_zbxo = 0
                for var_rdmc in arg_osiz:
                    var_llti += arg_rcsn[var_zbxo:var_zbxo + var_rdmc] + '.'
                    var_zbxo += var_rdmc
                var_llti += arg_rcsn[arg_wrnh:]
                arg_ayzf.append(var_llti)
            return
        for var_rjut in var_lsgw(1, var_cbvh(4, var_wnki + 1)):
            arg_osiz.append(var_rjut)
            if arg_xdvx.valid(arg_rcsn, arg_wrnh, var_rjut):
                arg_xdvx.helper(arg_rcsn, arg_wrnh + var_rjut, arg_osiz,
                    arg_ayzf)
            arg_osiz.pop()

    def func_yjch(arg_xdvx, arg_rcsn):
        var_dmio = []
        arg_xdvx.helper(arg_rcsn, 0, [], var_dmio)
        return var_dmio
