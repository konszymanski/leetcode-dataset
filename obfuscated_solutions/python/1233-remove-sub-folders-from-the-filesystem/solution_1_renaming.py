class Solution:

    def func_udax(arg_ihhe, arg_xdvx) ->var_wnki[var_egyk]:
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = []
        for var_rgwu in arg_xdvx:
            var_wrnh = False
            var_osiz = var_rgwu
            while not var_osiz == '':
                var_ayzf = var_osiz.rfind('/')
                if var_ayzf == -1:
                    break
                var_osiz = var_osiz[0:var_ayzf]
                if var_osiz in var_rcsn:
                    var_wrnh = True
                    break
            if not var_wrnh:
                var_hqta.append(var_rgwu)
        return var_hqta
