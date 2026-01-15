class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = 0
        var_hqta = var_rgwu(arg_xdvx) - 1
        var_wrnh = var_rgwu(arg_xdvx)
        while var_bacg <= var_hqta:
            var_osiz = (var_bacg + var_hqta) // 2
            if arg_xdvx[var_osiz] >= arg_rcsn:
                var_wrnh = var_osiz
                var_hqta = var_osiz - 1
            else:
                var_bacg = var_osiz + 1
        return var_wrnh

    def func_ayzf(arg_ihhe, arg_xdvx: var_wnki[var_egyk]) ->var_egyk:
        arg_xdvx.sort()
        var_dcmd = var_rgwu(arg_xdvx)
        for var_llti in var_zbxo(1, var_dcmd + 1):
            var_rdmc = arg_ihhe.get_first_greater_or_equal(arg_xdvx, var_llti)
            if var_dcmd - var_rdmc == var_llti:
                return var_llti
        return -1
