class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh()
        var_osiz = var_wrnh()
        var_ayzf = 0
        var_wnki = 0
        for var_egyk in var_dcmd(var_llti(arg_xdvx)):
            while var_rgwu and var_rgwu[-1] < arg_xdvx[var_egyk]:
                var_rgwu.pop()
            var_rgwu.append(arg_xdvx[var_egyk])
            while var_osiz and var_osiz[-1] > arg_xdvx[var_egyk]:
                var_osiz.pop()
            var_osiz.append(arg_xdvx[var_egyk])
            while var_rgwu[0] - var_osiz[0] > arg_rcsn:
                if var_rgwu[0] == arg_xdvx[var_ayzf]:
                    var_rgwu.popleft()
                if var_osiz[0] == arg_xdvx[var_ayzf]:
                    var_osiz.popleft()
                var_ayzf += 1
            var_wnki = var_zbxo(var_wnki, var_egyk - var_ayzf + 1)
        return var_wnki
