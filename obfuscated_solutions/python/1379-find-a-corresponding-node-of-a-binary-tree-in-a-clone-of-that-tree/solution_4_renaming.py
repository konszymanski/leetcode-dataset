class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:
        var_rgwu, var_wrnh = [], []
        var_osiz, var_ayzf = arg_xdvx, arg_rcsn
        while var_rgwu or var_ayzf:
            while var_osiz:
                var_rgwu.append(var_osiz)
                var_wrnh.append(var_ayzf)
                var_osiz = var_osiz.left
                var_ayzf = var_ayzf.left
            var_osiz = var_rgwu.pop()
            var_ayzf = var_wrnh.pop()
            if var_osiz is arg_bacg:
                return var_ayzf
            var_osiz = var_osiz.right
            var_ayzf = var_ayzf.right
