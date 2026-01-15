class Spreadsheet:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn):
        arg_ihhe.cell_values = {}

    def func_bacg(arg_ihhe, arg_hqta: var_wrnh, arg_rgwu: var_rcsn) ->None:
        arg_ihhe.cell_values[arg_hqta] = arg_rgwu

    def func_osiz(arg_ihhe, arg_hqta: var_wrnh) ->None:
        if arg_hqta in arg_ihhe.cell_values:
            del arg_ihhe.cell_values[arg_hqta]

    def func_ayzf(arg_ihhe, arg_wnki: var_wrnh) ->var_rcsn:
        var_egyk = arg_wnki.find('+')
        var_dcmd = arg_wnki[1:var_egyk]
        var_llti = arg_wnki[var_egyk + 1:]
        var_zbxo = arg_ihhe.cell_values.get(var_dcmd, 0) if var_dcmd[0
            ].isalpha() else var_rcsn(var_dcmd)
        var_rdmc = arg_ihhe.cell_values.get(var_llti, 0) if var_llti[0
            ].isalpha() else var_rcsn(var_llti)
        return var_zbxo + var_rdmc
