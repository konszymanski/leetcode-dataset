class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_llti[var_zbxo]:

        def func_hqta(arg_rgwu):
            nonlocal max_streak, curr_streak, curr_num, ans
            if arg_rgwu == var_wrnh:
                var_osiz += 1
            else:
                var_osiz = 1
                var_wrnh = arg_rgwu
            if var_osiz > var_ayzf:
                var_wnki = []
                var_ayzf = var_osiz
            if var_osiz == var_ayzf:
                var_wnki.append(arg_rgwu)
        var_ayzf = 0
        var_osiz = 0
        var_wrnh = 0
        var_wnki = []
        var_egyk = arg_xdvx
        while var_egyk:
            if var_egyk.left:
                var_dcmd = var_egyk.left
                while var_dcmd.right and var_dcmd.right != var_egyk:
                    var_dcmd = var_dcmd.right
                if not var_dcmd.right:
                    var_dcmd.right = var_egyk
                    var_egyk = var_egyk.left
                else:
                    var_dcmd.right = None
                    func_hqta(var_egyk.val)
                    var_egyk = var_egyk.right
            else:
                func_hqta(var_egyk.val)
                var_egyk = var_egyk.right
        return var_wnki
