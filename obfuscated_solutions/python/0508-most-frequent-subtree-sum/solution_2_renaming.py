class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_llti[var_wnki]:
        arg_ihhe.sum_freq = {}
        arg_ihhe.max_freq = 0

        def func_hqta(arg_xdvx) ->var_wnki:
            if not arg_xdvx:
                return 0
            var_rgwu = func_hqta(arg_xdvx.left)
            var_wrnh = func_hqta(arg_xdvx.right)
            var_osiz = arg_xdvx.val + var_rgwu + var_wrnh
            arg_ihhe.sum_freq[var_osiz] = arg_ihhe.sum_freq.get(var_osiz, 0
                ) + 1
            arg_ihhe.max_freq = var_ayzf(arg_ihhe.max_freq, arg_ihhe.
                sum_freq[var_osiz])
            return var_osiz
        func_hqta(arg_xdvx)
        var_egyk = []
        for var_dcmd in arg_ihhe.sum_freq:
            if arg_ihhe.sum_freq[var_dcmd] == arg_ihhe.max_freq:
                var_egyk.append(var_dcmd)
        return var_egyk
