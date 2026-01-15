class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = [([-1] * var_hqta(arg_rcsn)) for var_rgwu in var_wrnh(
            var_hqta(arg_xdvx[0]))]
        var_osiz = [([0] * 26) for var_rgwu in var_wrnh(var_hqta(arg_xdvx[0]))]
        for var_ayzf in var_wrnh(var_hqta(arg_xdvx)):
            for var_wnki in var_wrnh(var_hqta(arg_xdvx[0])):
                var_egyk = var_dcmd(arg_xdvx[var_ayzf][var_wnki]) - 97
                var_osiz[var_wnki][var_egyk] += 1
        return arg_ihhe.__get_words(arg_xdvx, arg_rcsn, 0, 0, var_bacg,
            var_osiz)

    def func_llti(arg_ihhe, arg_xdvx, arg_rcsn, arg_zbxo, arg_rdmc,
        var_bacg, var_osiz):
        if arg_rdmc == var_hqta(arg_rcsn):
            return 1
        if arg_zbxo == var_hqta(arg_xdvx[0]) or var_hqta(arg_xdvx[0]
            ) - arg_zbxo < var_hqta(arg_rcsn) - arg_rdmc:
            return 0
        if var_bacg[arg_zbxo][arg_rdmc] != -1:
            return var_bacg[arg_zbxo][arg_rdmc]
        var_rjut = 0
        var_lsgw = var_dcmd(arg_rcsn[arg_rdmc]) - 97
        var_rjut += arg_ihhe.__get_words(arg_xdvx, arg_rcsn, arg_zbxo + 1,
            arg_rdmc, var_bacg, var_osiz)
        var_rjut += var_osiz[arg_zbxo][var_lsgw] * arg_ihhe.__get_words(
            arg_xdvx, arg_rcsn, arg_zbxo + 1, arg_rdmc + 1, var_bacg, var_osiz)
        var_bacg[arg_zbxo][arg_rdmc] = var_rjut % 1000000007
        return var_bacg[arg_zbxo][arg_rdmc]
