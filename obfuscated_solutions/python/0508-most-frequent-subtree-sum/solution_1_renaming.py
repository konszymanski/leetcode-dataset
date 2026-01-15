class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_egyk[var_dcmd]:
        arg_ihhe.sum_freq = {}
        arg_ihhe.max_freq = 0

        def func_hqta(arg_xdvx):
            if not arg_xdvx:
                return 0
            return arg_xdvx.val + func_hqta(arg_xdvx.left) + func_hqta(arg_xdvx
                .right)

        def func_rgwu(arg_xdvx):
            if not arg_xdvx:
                return
            var_wrnh = func_hqta(arg_xdvx)
            arg_ihhe.sum_freq[var_wrnh] = arg_ihhe.sum_freq.get(var_wrnh, 0
                ) + 1
            arg_ihhe.max_freq = var_osiz(arg_ihhe.max_freq, arg_ihhe.
                sum_freq[var_wrnh])
            func_rgwu(arg_xdvx.left)
            func_rgwu(arg_xdvx.right)
        func_rgwu(arg_xdvx)
        var_ayzf = []
        for var_wnki in arg_ihhe.sum_freq:
            if arg_ihhe.sum_freq[var_wnki] == arg_ihhe.max_freq:
                var_ayzf.append(var_wnki)
        return var_ayzf
