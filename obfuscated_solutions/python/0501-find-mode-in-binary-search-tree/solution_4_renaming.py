class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_llti[var_zbxo]:

        def func_hqta(arg_rgwu, arg_wrnh):
            if not arg_rgwu:
                return
            func_hqta(arg_rgwu.left, values)
            values.append(arg_rgwu.val)
            func_hqta(arg_rgwu.right, values)
        values = []
        func_hqta(arg_xdvx, values)
        var_osiz = 0
        var_ayzf = 0
        var_wnki = 0
        var_egyk = []
        for var_dcmd in values:
            if var_dcmd == var_wnki:
                var_ayzf += 1
            else:
                var_ayzf = 1
                var_wnki = var_dcmd
            if var_ayzf > var_osiz:
                var_egyk = []
                var_osiz = var_ayzf
            if var_ayzf == var_osiz:
                var_egyk.append(var_dcmd)
        return var_egyk
