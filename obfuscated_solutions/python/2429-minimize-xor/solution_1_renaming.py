class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = arg_xdvx
        var_rgwu = var_wrnh(arg_rcsn).count('1')
        var_osiz = var_wrnh(var_hqta).count('1')
        var_ayzf = 0
        while var_osiz < var_rgwu:
            if not arg_ihhe._is_set(var_hqta, var_ayzf):
                var_hqta = arg_ihhe._set_bit(var_hqta, var_ayzf)
                var_osiz += 1
            var_ayzf += 1
        while var_osiz > var_rgwu:
            if arg_ihhe._is_set(var_hqta, var_ayzf):
                var_hqta = arg_ihhe._unset_bit(var_hqta, var_ayzf)
                var_osiz -= 1
            var_ayzf += 1
        return var_hqta

    def func_wnki(arg_ihhe, arg_egyk: var_bacg, arg_dcmd: var_bacg) ->var_llti:
        return arg_egyk & 1 << arg_dcmd != 0

    def func_zbxo(arg_ihhe, arg_egyk: var_bacg, arg_dcmd: var_bacg):
        return arg_egyk | 1 << arg_dcmd

    def func_rdmc(arg_ihhe, arg_egyk: var_bacg, arg_dcmd: var_bacg):
        return arg_egyk & ~(1 << arg_dcmd)
