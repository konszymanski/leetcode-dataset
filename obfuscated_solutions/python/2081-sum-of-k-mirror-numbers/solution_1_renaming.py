class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:

        def func_hqta(arg_rgwu: var_bacg) ->var_ayzf:
            var_wrnh = var_osiz()
            while arg_rgwu:
                var_wrnh.append(arg_rgwu % arg_xdvx)
                arg_rgwu //= arg_xdvx
            return var_wrnh == var_wrnh[::-1]
        var_wnki, var_egyk, var_dcmd = 1, 0, 0
        while var_egyk < arg_rcsn:
            var_llti = var_wnki * 10
            for var_zbxo in [0, 1]:
                for var_rdmc in var_rjut(var_wnki, var_llti):
                    if var_egyk == arg_rcsn:
                        break
                    var_lsgw = var_rdmc
                    arg_rgwu = var_rdmc // 10 if var_zbxo == 0 else var_rdmc
                    while arg_rgwu:
                        var_lsgw = var_lsgw * 10 + arg_rgwu % 10
                        arg_rgwu //= 10
                    if func_hqta(var_lsgw):
                        var_egyk += 1
                        var_dcmd += var_lsgw
            var_wnki = var_llti
        return var_dcmd
