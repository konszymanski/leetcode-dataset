class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu = 0
        var_wrnh = var_osiz = 0
        var_ayzf = var_wnki = arg_xdvx[var_hqta]
        for var_hqta in var_egyk(var_dcmd(arg_xdvx)):
            var_ayzf = var_llti(var_ayzf, arg_xdvx[var_hqta])
            var_wnki = var_zbxo(var_wnki, arg_xdvx[var_hqta])
            if var_wnki - var_ayzf > 2:
                var_wrnh = var_hqta - var_rgwu
                var_osiz += var_wrnh * (var_wrnh + 1) // 2
                var_rgwu = var_hqta
                var_ayzf = var_wnki = arg_xdvx[var_hqta]
                while var_rgwu > 0 and var_rdmc(arg_xdvx[var_hqta] -
                    arg_xdvx[var_rgwu - 1]) <= 2:
                    var_rgwu -= 1
                    var_ayzf = var_llti(var_ayzf, arg_xdvx[var_rgwu])
                    var_wnki = var_zbxo(var_wnki, arg_xdvx[var_rgwu])
                if var_rgwu < var_hqta:
                    var_wrnh = var_hqta - var_rgwu
                    var_osiz -= var_wrnh * (var_wrnh + 1) // 2
        var_wrnh = var_hqta - var_rgwu + 1
        var_osiz += var_wrnh * (var_wrnh + 1) // 2
        return var_osiz
