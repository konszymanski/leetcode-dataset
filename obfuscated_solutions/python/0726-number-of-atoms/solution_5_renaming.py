class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 1
        var_hqta = [1]
        var_rgwu = var_wrnh(var_osiz)
        var_ayzf = ''
        var_wnki = ''
        var_egyk = var_dcmd(arg_xdvx) - 1
        while var_egyk >= 0:
            if arg_xdvx[var_egyk].isdigit():
                var_wnki = arg_xdvx[var_egyk] + var_wnki
            elif arg_xdvx[var_egyk].islower():
                var_ayzf = arg_xdvx[var_egyk] + var_ayzf
            elif arg_xdvx[var_egyk].isupper():
                var_ayzf = arg_xdvx[var_egyk] + var_ayzf
                if var_wnki:
                    var_rgwu[var_ayzf] += var_osiz(var_wnki) * var_bacg
                else:
                    var_rgwu[var_ayzf] += 1 * var_bacg
                var_ayzf = ''
                var_wnki = ''
            elif arg_xdvx[var_egyk] == ')':
                var_llti = var_osiz(var_wnki) if var_wnki else 1
                var_hqta.append(var_llti)
                var_bacg *= var_llti
                var_wnki = ''
            elif arg_xdvx[var_egyk] == '(':
                var_bacg //= var_hqta.pop()
            var_egyk -= 1
        var_rgwu = var_zbxo(var_rdmc(var_rgwu.items()))
        var_rjut = ''
        for var_lsgw in var_rgwu:
            var_rjut += var_lsgw
            if var_rgwu[var_lsgw] > 1:
                var_rjut += var_rcsn(var_rgwu[var_lsgw])
        return var_rjut
