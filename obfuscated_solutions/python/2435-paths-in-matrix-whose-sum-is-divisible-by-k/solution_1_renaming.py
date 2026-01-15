class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = 10 ** 9 + 7
        var_wrnh, var_osiz = var_ayzf(arg_xdvx), var_ayzf(arg_xdvx[0])
        var_wnki = [[([0] * arg_rcsn) for var_egyk in var_dcmd(var_osiz + 1
            )] for var_egyk in var_dcmd(var_wrnh + 1)]
        for var_llti in var_dcmd(1, var_wrnh + 1):
            for var_zbxo in var_dcmd(1, var_osiz + 1):
                if var_llti == 1 and var_zbxo == 1:
                    var_wnki[var_llti][var_zbxo][arg_xdvx[0][0] % arg_rcsn] = 1
                    continue
                var_rdmc = arg_xdvx[var_llti - 1][var_zbxo - 1] % arg_rcsn
                for var_rjut in var_dcmd(arg_rcsn):
                    var_lsgw = (var_rjut - var_rdmc + arg_rcsn) % arg_rcsn
                    var_wnki[var_llti][var_zbxo][var_rjut] = (var_wnki[
                        var_llti - 1][var_zbxo][var_lsgw] + var_wnki[
                        var_llti][var_zbxo - 1][var_lsgw]) % var_rgwu
        return var_wnki[var_wrnh][var_osiz][0]
