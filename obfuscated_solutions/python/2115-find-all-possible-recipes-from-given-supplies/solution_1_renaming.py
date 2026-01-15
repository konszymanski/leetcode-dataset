class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_hqta[var_rgwu]], arg_bacg: var_hqta[var_rgwu]) ->var_hqta[
        var_rgwu]:
        var_wrnh = var_osiz(arg_bacg)
        var_ayzf = var_wnki(var_egyk(var_dcmd(arg_xdvx)))
        var_llti = []
        var_zbxo = -1
        while var_dcmd(var_wrnh) > var_zbxo:
            var_zbxo = var_dcmd(var_wrnh)
            var_rdmc = var_dcmd(var_ayzf)
            while var_rdmc > 0:
                var_rdmc -= 1
                var_rjut = var_ayzf.popleft()
                if var_lsgw(var_cbvh in var_wrnh for var_cbvh in arg_rcsn[
                    var_rjut]):
                    var_wrnh.add(arg_xdvx[var_rjut])
                    var_llti.append(arg_xdvx[var_rjut])
                else:
                    var_ayzf.append(var_rjut)
        return var_llti
