class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        var_hqta = var_rgwu(var_wrnh)
        for var_osiz, var_ayzf in arg_xdvx:
            var_hqta[var_osiz].append(var_ayzf)
            var_hqta[var_ayzf].append(var_osiz)
        var_wnki = None
        for var_egyk in var_hqta:
            if var_dcmd(var_hqta[var_egyk]) == 1:
                var_wnki = var_egyk
                break

        def func_llti(arg_zbxo, arg_rdmc, arg_rjut):
            arg_rjut.append(arg_zbxo)
            for var_lsgw in var_hqta[arg_zbxo]:
                if var_lsgw != arg_rdmc:
                    func_llti(var_lsgw, arg_zbxo, arg_rjut)
        arg_rjut = []
        func_llti(var_wnki, None, arg_rjut)
        return arg_rjut
