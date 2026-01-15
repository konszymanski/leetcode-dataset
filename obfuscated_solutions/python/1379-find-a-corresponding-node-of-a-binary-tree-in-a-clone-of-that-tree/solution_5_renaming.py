class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:
        var_rgwu = var_wrnh([arg_xdvx])
        var_osiz = var_wrnh([arg_rcsn])
        while var_rgwu:
            var_ayzf = var_rgwu.popleft()
            var_wnki = var_osiz.popleft()
            if var_ayzf is arg_bacg:
                return var_wnki
            if var_ayzf:
                var_rgwu.append(var_ayzf.left)
                var_rgwu.append(var_ayzf.right)
                var_osiz.append(var_wnki.left)
                var_osiz.append(var_wnki.right)
