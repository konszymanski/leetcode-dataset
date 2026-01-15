class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        items.sort(key=lambda x: var_rgwu[0])
        var_wrnh = items[0][1]
        for var_osiz in var_ayzf(var_wnki(items)):
            var_wrnh = var_egyk(var_wrnh, items[var_osiz][1])
            items[var_osiz][1] = var_wrnh
        return [arg_ihhe.binary_search(items, var_dcmd) for var_dcmd in
            arg_rcsn]

    def func_llti(arg_ihhe, arg_xdvx, arg_zbxo):
        var_rdmc, var_rjut = 0, var_wnki(items) - 1
        var_wrnh = 0
        while var_rdmc <= var_rjut:
            var_lsgw = (var_rdmc + var_rjut) // 2
            if items[var_lsgw][0] > arg_zbxo:
                var_rjut = var_lsgw - 1
            else:
                var_wrnh = var_egyk(var_wrnh, items[var_lsgw][1])
                var_rdmc = var_lsgw + 1
        return var_wrnh
