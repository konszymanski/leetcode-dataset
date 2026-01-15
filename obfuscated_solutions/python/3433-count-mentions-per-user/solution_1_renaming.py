class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_rgwu]]) ->var_hqta[var_bacg]:
        arg_rcsn.sort(key=lambda e: (var_bacg(var_wrnh[1]), var_wrnh[0] ==
            'MESSAGE'))
        var_osiz = [0] * arg_xdvx
        var_ayzf = [0] * arg_xdvx
        for var_wnki in arg_rcsn:
            var_egyk = var_bacg(var_wnki[1])
            if var_wnki[0] == 'MESSAGE':
                if var_wnki[2] == 'ALL':
                    for var_dcmd in var_llti(arg_xdvx):
                        var_osiz[var_dcmd] += 1
                elif var_wnki[2] == 'HERE':
                    for var_dcmd, var_zbxo in var_rdmc(var_ayzf):
                        if var_zbxo <= var_egyk:
                            var_osiz[var_dcmd] += 1
                else:
                    for var_rjut in var_wnki[2].split():
                        var_osiz[var_bacg(var_rjut[2:])] += 1
            else:
                var_ayzf[var_bacg(var_wnki[2])] = var_egyk + 60
        return var_osiz
