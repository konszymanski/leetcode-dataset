class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        while arg_rcsn < arg_bacg:
            var_rgwu = arg_rcsn + (arg_bacg - arg_rcsn) // 2
            if arg_xdvx[var_rgwu] >= arg_hqta:
                arg_bacg = var_rgwu
            else:
                arg_rcsn = var_rgwu + 1
        return arg_rcsn

    def func_wrnh(arg_ihhe, arg_xdvx):
        var_osiz = var_ayzf(arg_xdvx)
        arg_rcsn, arg_bacg = 0, var_osiz - 1
        while arg_rcsn + 1 < var_osiz and arg_xdvx[arg_rcsn] <= arg_xdvx[
            arg_rcsn + 1]:
            arg_rcsn += 1
        while arg_bacg - 1 >= 0 and arg_xdvx[arg_bacg] >= arg_xdvx[arg_bacg - 1
            ]:
            arg_bacg -= 1
        if arg_rcsn >= arg_bacg:
            return 0
        var_wnki = var_egyk(var_osiz - (arg_rcsn + 1), arg_bacg)
        for var_dcmd in var_llti(arg_rcsn + 1):
            var_zbxo = arg_ihhe.helper_binary_search(arg_xdvx, arg_bacg,
                var_osiz, arg_xdvx[var_dcmd])
            var_wnki = var_egyk(var_wnki, var_zbxo - (var_dcmd + 1))
        return var_wnki
