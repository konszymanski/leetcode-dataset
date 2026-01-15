class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: 'ListNode') ->var_rjut[var_rjut[var_hqta]]:
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = 0
        var_ayzf = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        var_wnki = [[(-1) for var_egyk in var_dcmd(arg_rcsn)] for var_egyk in
            var_dcmd(arg_xdvx)]
        while arg_bacg is not None:
            var_wnki[var_rgwu][var_wrnh] = arg_bacg.val
            var_llti = var_rgwu + var_ayzf[var_osiz][0]
            var_zbxo = var_wrnh + var_ayzf[var_osiz][1]
            if var_rdmc(var_llti, var_zbxo
                ) < 0 or var_llti >= arg_xdvx or var_zbxo >= arg_rcsn or var_wnki[
                var_llti][var_zbxo] != -1:
                var_osiz = (var_osiz + 1) % 4
            var_rgwu += var_ayzf[var_osiz][0]
            var_wrnh += var_ayzf[var_osiz][1]
            arg_bacg = arg_bacg.next
        return var_wnki
