class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_dcmd[var_llti]:

        def func_hqta(arg_rgwu):
            nonlocal max_streak, curr_streak, curr_num, ans
            if not arg_rgwu:
                return
            func_hqta(arg_rgwu.left)
            var_wrnh = arg_rgwu.val
            if var_wrnh == var_osiz:
                var_ayzf += 1
            else:
                var_ayzf = 1
                var_osiz = var_wrnh
            if var_ayzf > var_wnki:
                var_egyk = []
                var_wnki = var_ayzf
            if var_ayzf == var_wnki:
                var_egyk.append(var_wrnh)
            func_hqta(arg_rgwu.right)
        var_wnki = 0
        var_ayzf = 0
        var_osiz = 0
        var_egyk = []
        func_hqta(arg_xdvx)
        return var_egyk
