class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_hqta[var_bacg]:
        var_rgwu = var_wrnh(arg_rcsn)
        var_osiz = []
        arg_ihhe._backtrack(arg_xdvx, var_rgwu, [], var_osiz, 0)
        return var_osiz

    def func_ayzf(arg_ihhe, arg_xdvx: var_bacg, var_rgwu: var_wrnh,
        arg_wnki: var_hqta[var_bacg], var_osiz: var_hqta[var_bacg],
        arg_egyk: var_dcmd):
        if arg_egyk == var_llti(arg_xdvx):
            var_osiz.append(' '.join(arg_wnki))
            return
        for var_zbxo in var_rdmc(arg_egyk + 1, var_llti(arg_xdvx) + 1):
            var_rjut = arg_xdvx[arg_egyk:var_zbxo]
            if var_rjut in var_rgwu:
                arg_wnki.append(var_rjut)
                arg_ihhe._backtrack(arg_xdvx, var_rgwu, arg_wnki, var_osiz,
                    var_zbxo)
                arg_wnki.pop()
