var_udax = 10 ** 9 + 7
var_ihhe = 10 ** 4 + 10
var_xdvx = 15
var_rcsn = [0] * var_ihhe
for var_bacg in var_hqta(2, var_ihhe):
    if var_rcsn[var_bacg] == 0:
        for var_rgwu in var_hqta(var_bacg, var_ihhe, var_bacg):
            var_rcsn[var_rgwu] = var_bacg
var_wrnh = [[] for var_osiz in var_hqta(var_ihhe)]
for var_bacg in var_hqta(2, var_ihhe):
    var_ayzf = var_bacg
    while var_ayzf > 1:
        var_wnki = var_rcsn[var_ayzf]
        var_egyk = 0
        while var_ayzf % var_wnki == 0:
            var_ayzf //= var_wnki
            var_egyk += 1
        var_wrnh[var_bacg].append(var_egyk)
var_dcmd = [([0] * (var_xdvx + 1)) for var_osiz in var_hqta(var_ihhe +
    var_xdvx)]
var_dcmd[0][0] = 1
for var_bacg in var_hqta(1, var_ihhe + var_xdvx):
    var_dcmd[var_bacg][0] = 1
    for var_rgwu in var_hqta(1, var_llti(var_bacg, var_xdvx) + 1):
        var_dcmd[var_bacg][var_rgwu] = (var_dcmd[var_bacg - 1][var_rgwu] +
            var_dcmd[var_bacg - 1][var_rgwu - 1]) % var_udax


class Solution:

    def func_zbxo(arg_rdmc, arg_rjut: var_cbvh, arg_lsgw: var_cbvh) ->var_cbvh:
        var_yjch = 0
        for var_ayzf in var_hqta(1, arg_lsgw + 1):
            var_dmio = 1
            for var_wnki in var_wrnh[var_ayzf]:
                var_dmio = var_dmio * var_dcmd[arg_rjut + var_wnki - 1][
                    var_wnki] % var_udax
            var_yjch = (var_yjch + var_dmio) % var_udax
        return var_yjch
