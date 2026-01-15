class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:

        def func_hqta(arg_xdvx):
            if not arg_xdvx:
                return 0, None
            var_rgwu = func_hqta(arg_xdvx.left)
            var_wrnh = func_hqta(arg_xdvx.right)
            if var_rgwu[0] > var_wrnh[0]:
                return var_rgwu[0] + 1, var_rgwu[1]
            if var_rgwu[0] < var_wrnh[0]:
                return var_wrnh[0] + 1, var_wrnh[1]
            return var_rgwu[0] + 1, arg_xdvx
        return func_hqta(arg_xdvx)[1]
