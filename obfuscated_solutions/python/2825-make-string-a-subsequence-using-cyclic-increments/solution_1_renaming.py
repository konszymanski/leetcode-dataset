class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_dcmd:
        var_hqta = var_rgwu(arg_xdvx)
        for var_wrnh in var_osiz(1 << var_hqta):
            var_ayzf = var_wnki(arg_xdvx)
            for var_egyk in var_osiz(var_hqta):
                if var_wrnh & 1 << var_egyk != 0:
                    var_ayzf[var_egyk] = arg_ihhe._get_next_char(var_ayzf[
                        var_egyk])
            if arg_ihhe._is_subsequence(''.join(var_ayzf), arg_rcsn):
                return True
        return False

    def func_llti(arg_ihhe, arg_zbxo: var_bacg) ->var_bacg:
        return 'a' if arg_zbxo == 'z' else var_rdmc(var_rjut(arg_zbxo) + 1)

    def func_lsgw(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_dcmd:
        var_egyk, var_cbvh = 0, 0
        var_hqta, var_yjch = var_rgwu(arg_xdvx), var_rgwu(arg_rcsn)
        while var_egyk < var_hqta and var_cbvh < var_yjch:
            if arg_xdvx[var_egyk] == arg_rcsn[var_cbvh]:
                var_cbvh += 1
            var_egyk += 1
        return var_cbvh == var_yjch
