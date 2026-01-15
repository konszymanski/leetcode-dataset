class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = 0

        def func_hqta(arg_rgwu):
            nonlocal total_tilt
            if not arg_rgwu:
                return 0
            var_wrnh = func_hqta(arg_rgwu.left)
            var_osiz = func_hqta(arg_rgwu.right)
            var_ayzf = var_wnki(var_wrnh - var_osiz)
            var_bacg += var_ayzf
            return var_wrnh + var_osiz + arg_rgwu.val
        func_hqta(arg_xdvx)
        return var_bacg
