class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 0
        for var_rgwu in var_wrnh(arg_xdvx, arg_rcsn + 1):
            if var_rgwu < 100 and var_rgwu % 11 == 0:
                var_hqta += 1
            if 1000 <= var_rgwu < 10000:
                var_osiz = var_rgwu // 1000 + var_rgwu % 1000 // 100
                var_ayzf = var_rgwu % 100 // 10 + var_rgwu % 10
                if var_osiz == var_ayzf:
                    var_hqta += 1
        return var_hqta
