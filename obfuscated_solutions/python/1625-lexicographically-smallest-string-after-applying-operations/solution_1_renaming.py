class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu) ->var_hqta:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [False] * var_wrnh
        var_wnki = arg_xdvx
        arg_xdvx = arg_xdvx + arg_xdvx
        var_egyk = 0
        while not var_ayzf[var_egyk]:
            var_ayzf[var_egyk] = True
            for var_dcmd in var_llti(10):
                var_zbxo = 0 if arg_bacg % 2 == 0 else 9
                for var_rdmc in var_llti(var_zbxo + 1):
                    var_rjut = var_lsgw(arg_xdvx[var_egyk:var_egyk + var_wrnh])
                    for var_cbvh in var_llti(1, var_wrnh, 2):
                        var_rjut[var_cbvh] = var_hqta((var_rgwu(var_rjut[
                            var_cbvh]) + var_dcmd * arg_rcsn) % 10)
                    for var_cbvh in var_llti(0, var_wrnh, 2):
                        var_rjut[var_cbvh] = var_hqta((var_rgwu(var_rjut[
                            var_cbvh]) + var_rdmc * arg_rcsn) % 10)
                    var_yjch = ''.join(var_rjut)
                    if var_yjch < var_wnki:
                        var_wnki = var_yjch
            var_egyk = (var_egyk + arg_bacg) % var_wrnh
        return var_wnki
