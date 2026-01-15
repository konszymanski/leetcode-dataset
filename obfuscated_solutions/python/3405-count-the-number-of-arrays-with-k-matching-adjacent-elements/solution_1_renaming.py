var_udax = 10 ** 9 + 7
var_ihhe = 10 ** 5
var_xdvx = [0] * var_ihhe
var_rcsn = [0] * var_ihhe


def func_bacg(arg_hqta, arg_rgwu):
    var_wrnh = 1
    while arg_rgwu:
        if arg_rgwu & 1:
            var_wrnh = var_wrnh * arg_hqta % var_udax
        arg_hqta = arg_hqta * arg_hqta % var_udax
        arg_rgwu >>= 1
    return var_wrnh


def func_osiz():
    if var_xdvx[0] != 0:
        return
    var_xdvx[0] = 1
    for var_ayzf in var_wnki(1, var_ihhe):
        var_xdvx[var_ayzf] = var_xdvx[var_ayzf - 1] * var_ayzf % var_udax
    var_rcsn[var_ihhe - 1] = func_bacg(var_xdvx[var_ihhe - 1], var_udax - 2)
    for var_ayzf in var_wnki(var_ihhe - 1, 0, -1):
        var_rcsn[var_ayzf - 1] = var_rcsn[var_ayzf] * var_ayzf % var_udax


def func_egyk(arg_rgwu, arg_dcmd):
    return var_xdvx[arg_rgwu] * var_rcsn[arg_dcmd] % var_udax * var_rcsn[
        arg_rgwu - arg_dcmd] % var_udax


class Solution:

    def func_llti(arg_zbxo, arg_rgwu: var_rjut, arg_dcmd: var_rjut,
        arg_rdmc: var_rjut) ->var_rjut:
        func_osiz()
        return func_egyk(arg_rgwu - 1, arg_rdmc
            ) * arg_dcmd % var_udax * func_bacg(arg_dcmd - 1, arg_rgwu -
            arg_rdmc - 1) % var_udax
