class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_llti[var_zbxo]:
        var_hqta = 0
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = []
        var_ayzf = arg_xdvx
        while var_ayzf:
            if var_ayzf.left:
                var_wnki = var_ayzf.left
                while var_wnki.right:
                    var_wnki = var_wnki.right
                var_wnki.right = var_ayzf
                var_egyk = var_ayzf.left
                var_ayzf.left = None
                var_ayzf = var_egyk
            else:
                var_dcmd = var_ayzf.val
                if var_dcmd == var_wrnh:
                    var_rgwu += 1
                else:
                    var_rgwu = 1
                    var_wrnh = var_dcmd
                if var_rgwu > var_hqta:
                    var_osiz = []
                    var_hqta = var_rgwu
                if var_rgwu == var_hqta:
                    var_osiz.append(var_dcmd)
                var_ayzf = var_ayzf.right
        return var_osiz
