class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = arg_ihhe._compute_longest_prefix_suffix(arg_rcsn)
        var_rgwu = []
        var_wrnh = [0] * (var_osiz(arg_xdvx) + 1)
        var_ayzf = 0
        var_wnki = 0
        while var_ayzf < var_osiz(arg_xdvx):
            var_egyk = arg_xdvx[var_ayzf]
            var_rgwu.append(var_egyk)
            if var_egyk == arg_rcsn[var_wnki]:
                var_wrnh[var_osiz(var_rgwu)] = var_wnki + 1
                var_wnki += 1
                if var_wnki == var_osiz(arg_rcsn):
                    for var_dcmd in var_llti(var_osiz(arg_rcsn)):
                        var_rgwu.pop()
                    var_wnki = 0 if not var_rgwu else var_wrnh[var_osiz(
                        var_rgwu)]
            elif var_wnki != 0:
                var_ayzf -= 1
                var_wnki = var_hqta[var_wnki - 1]
                var_rgwu.pop()
            else:
                var_wrnh[var_osiz(var_rgwu)] = 0
            var_ayzf += 1
        return ''.join(var_rgwu)

    def func_zbxo(arg_ihhe, arg_rdmc: var_bacg) ->var_yjch:
        var_rjut = [0] * var_osiz(arg_rdmc)
        var_lsgw = 1
        var_cbvh = 0
        while var_lsgw < var_osiz(arg_rdmc):
            if arg_rdmc[var_lsgw] == arg_rdmc[var_cbvh]:
                var_cbvh += 1
                var_rjut[var_lsgw] = var_cbvh
                var_lsgw += 1
            elif var_cbvh != 0:
                var_cbvh = var_rjut[var_cbvh - 1]
            else:
                var_rjut[var_lsgw] = 0
                var_lsgw += 1
        return var_rjut
