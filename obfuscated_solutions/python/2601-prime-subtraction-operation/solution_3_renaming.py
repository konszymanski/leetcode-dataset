class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = [1] * (var_rcsn + 1)
        var_hqta[1] = 0
        for var_rgwu in var_wrnh(2, var_osiz(var_ayzf.sqrt(var_rcsn + 1)) + 1):
            if var_hqta[var_rgwu] == 1:
                for var_wnki in var_wrnh(var_rgwu * var_rgwu, var_rcsn + 1,
                    var_rgwu):
                    var_hqta[var_wnki] = 0
        var_egyk = 1
        var_rgwu = 0
        while var_rgwu < var_dcmd(arg_xdvx):
            var_llti = arg_xdvx[var_rgwu] - var_egyk
            if var_llti < 0:
                return False
            if var_hqta[var_llti] or var_llti == 0:
                var_rgwu += 1
                var_egyk += 1
            else:
                var_egyk += 1
        return True
