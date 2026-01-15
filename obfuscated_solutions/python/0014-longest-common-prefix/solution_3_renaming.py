class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        if not arg_xdvx:
            return ''

        def func_rcsn(arg_bacg, arg_hqta):
            var_rgwu = var_wrnh(var_osiz(arg_bacg), var_osiz(arg_hqta))
            for var_ayzf in var_wnki(var_rgwu):
                if arg_bacg[var_ayzf] != arg_hqta[var_ayzf]:
                    return arg_bacg[:var_ayzf]
            return arg_bacg[:var_rgwu]

        def func_egyk(arg_xdvx, arg_dcmd, arg_llti):
            if arg_dcmd == arg_llti:
                return arg_xdvx[arg_dcmd]
            else:
                var_zbxo = (arg_dcmd + arg_llti) // 2
                var_rdmc = func_egyk(arg_xdvx, arg_dcmd, var_zbxo)
                var_rjut = func_egyk(arg_xdvx, var_zbxo + 1, arg_llti)
                return func_rcsn(var_rdmc, var_rjut)
        return func_egyk(arg_xdvx, 0, var_osiz(arg_xdvx) - 1)
