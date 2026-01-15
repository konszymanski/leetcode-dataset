class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_wnki:
        arg_ihhe.pathLength = 0

        def func_hqta(arg_rgwu, arg_wrnh, arg_osiz):
            if arg_rgwu:
                arg_ihhe.pathLength = var_ayzf(arg_ihhe.pathLength, arg_osiz)
                if arg_wrnh:
                    func_hqta(arg_rgwu.left, False, arg_osiz + 1)
                    func_hqta(arg_rgwu.right, True, 1)
                else:
                    func_hqta(arg_rgwu.left, False, 1)
                    func_hqta(arg_rgwu.right, True, arg_osiz + 1)
        func_hqta(arg_xdvx, True, 0)
        return arg_ihhe.pathLength
