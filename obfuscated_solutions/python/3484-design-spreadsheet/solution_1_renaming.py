class Spreadsheet:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn):
        arg_ihhe.grid = [([0] * 27) for var_bacg in var_hqta(arg_xdvx + 1)]

    def func_rgwu(arg_ihhe, arg_wrnh: var_ayzf, arg_osiz: var_rcsn) ->None:
        var_wnki, var_egyk = arg_ihhe.getPos(arg_wrnh)
        arg_ihhe.grid[var_wnki][var_egyk] = arg_osiz

    def func_dcmd(arg_ihhe, arg_wrnh: var_ayzf) ->None:
        var_wnki, var_egyk = arg_ihhe.getPos(arg_wrnh)
        arg_ihhe.grid[var_wnki][var_egyk] = 0

    def func_llti(arg_ihhe, arg_zbxo: var_ayzf) ->var_rcsn:
        var_rdmc = arg_zbxo.find('+')
        var_rjut = arg_zbxo[1:var_rdmc]
        var_lsgw = arg_zbxo[var_rdmc + 1:]
        return arg_ihhe.getCellVal(var_rjut) + arg_ihhe.getCellVal(var_lsgw)

    def func_cbvh(arg_ihhe, arg_wrnh):
        var_wnki = var_rcsn(arg_wrnh[1:])
        var_egyk = var_yjch(arg_wrnh[0]) - var_yjch('A')
        return var_wnki, var_egyk

    def func_dmio(arg_ihhe, arg_wrnh):
        if arg_wrnh[0].isalpha():
            var_wnki, var_egyk = arg_ihhe.getPos(arg_wrnh)
            return arg_ihhe.grid[var_wnki][var_egyk]
        else:
            return var_rcsn(arg_wrnh)
