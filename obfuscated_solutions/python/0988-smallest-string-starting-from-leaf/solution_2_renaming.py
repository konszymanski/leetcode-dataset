class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_llti:
        var_hqta = ''
        var_rgwu = var_wrnh()
        var_rgwu.append([arg_xdvx, var_osiz(arg_xdvx.val + var_ayzf('a'))])
        while var_rgwu:
            var_wnki, var_egyk = var_rgwu.popleft()
            if not var_wnki.left and not var_wnki.right:
                var_hqta = var_dcmd(var_hqta, var_egyk
                    ) if var_hqta else var_egyk
            if var_wnki.left:
                var_rgwu.append([var_wnki.left, var_osiz(var_wnki.left.val +
                    var_ayzf('a')) + var_egyk])
            if var_wnki.right:
                var_rgwu.append([var_wnki.right, var_osiz(var_wnki.right.
                    val + var_ayzf('a')) + var_egyk])
        return var_hqta
