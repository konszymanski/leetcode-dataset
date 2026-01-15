class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_egyk:
        var_hqta = 0
        var_rgwu = 0
        while var_hqta < var_wrnh(arg_xdvx):
            var_osiz = 1
            while var_hqta + var_osiz < var_wrnh(arg_xdvx) and arg_xdvx[
                var_hqta + var_osiz] == arg_xdvx[var_hqta]:
                var_osiz += 1
            arg_xdvx[var_rgwu] = arg_xdvx[var_hqta]
            var_rgwu += 1
            if var_osiz > 1:
                var_ayzf = var_bacg(var_osiz)
                arg_xdvx[var_rgwu:var_rgwu + var_wrnh(var_ayzf)] = var_wnki(
                    var_ayzf)
                var_rgwu += var_wrnh(var_ayzf)
            var_hqta += var_osiz
        return var_rgwu
