class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 10 ** 9 + 7
        var_ayzf = [0] * (var_rgwu + 1)
        var_wnki = [0] * (var_rgwu + 1)
        var_egyk = var_dcmd()
        var_llti = var_dcmd()
        var_ayzf[0] = 1
        var_wnki[0] = 1
        var_zbxo = 0
        for var_rdmc in var_rjut(var_rgwu):
            while var_llti and arg_xdvx[var_llti[-1]] <= arg_xdvx[var_rdmc]:
                var_llti.pop()
            var_llti.append(var_rdmc)
            while var_egyk and arg_xdvx[var_egyk[-1]] >= arg_xdvx[var_rdmc]:
                var_egyk.pop()
            var_egyk.append(var_rdmc)
            while var_llti and var_egyk and arg_xdvx[var_llti[0]] - arg_xdvx[
                var_egyk[0]] > arg_rcsn:
                if var_llti[0] == var_zbxo:
                    var_llti.popleft()
                if var_egyk[0] == var_zbxo:
                    var_egyk.popleft()
                var_zbxo += 1
            if var_zbxo > 0:
                var_ayzf[var_rdmc + 1] = (var_wnki[var_rdmc] - var_wnki[
                    var_zbxo - 1] + var_osiz) % var_osiz
            else:
                var_ayzf[var_rdmc + 1] = var_wnki[var_rdmc] % var_osiz
            var_wnki[var_rdmc + 1] = (var_wnki[var_rdmc] + var_ayzf[
                var_rdmc + 1]) % var_osiz
        return var_ayzf[var_rgwu]
