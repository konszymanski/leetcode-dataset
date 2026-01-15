class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        if not arg_xdvx:
            return False
        for var_rgwu in arg_xdvx:
            if var_rgwu != '_' and not var_rgwu.isalnum():
                return False
        return arg_rcsn

    def func_wrnh(arg_ihhe, arg_xdvx: var_ayzf[var_bacg], arg_osiz:
        var_ayzf[var_bacg], arg_rcsn: var_ayzf[var_hqta]) ->var_ayzf[var_bacg]:
        var_wnki = [[] for var_egyk in var_dcmd(4)]
        var_llti = []
        var_zbxo = {'electronics': 0, 'grocery': 1, 'pharmacy': 2,
            'restaurant': 3}
        for var_rdmc in var_dcmd(var_rjut(arg_xdvx)):
            if arg_xdvx[var_rdmc] and arg_ihhe.check(arg_xdvx[var_rdmc],
                arg_rcsn[var_rdmc]):
                var_lsgw = arg_osiz[var_rdmc]
                if var_lsgw in var_zbxo:
                    var_cbvh = var_zbxo[var_lsgw]
                    var_wnki[var_cbvh].append(arg_xdvx[var_rdmc])
        for var_yjch in var_wnki:
            var_yjch.sort()
            var_llti.extend(var_yjch)
        return var_llti
