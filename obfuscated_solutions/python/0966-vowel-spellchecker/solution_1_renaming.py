class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):

        def func_hqta(arg_rgwu):
            return ''.join('*' if var_wrnh in 'aeiou' else var_wrnh for
                var_wrnh in arg_rgwu)
        var_osiz = var_ayzf(arg_rcsn)
        var_wnki = {}
        var_egyk = {}
        for arg_rgwu in arg_rcsn:
            var_dcmd = arg_rgwu.lower()
            var_wnki.setdefault(var_dcmd, arg_rgwu)
            var_egyk.setdefault(func_hqta(var_dcmd), arg_rgwu)

        def func_llti(arg_zbxo):
            if arg_zbxo in var_osiz:
                return arg_zbxo
            var_rdmc = arg_zbxo.lower()
            if var_rdmc in var_wnki:
                return var_wnki[var_rdmc]
            var_rjut = func_hqta(var_rdmc)
            if var_rjut in var_egyk:
                return var_egyk[var_rjut]
            return ''
        return var_lsgw(func_llti, arg_bacg)
