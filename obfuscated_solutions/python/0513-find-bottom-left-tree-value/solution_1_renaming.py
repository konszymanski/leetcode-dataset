class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_hqta:
        arg_ihhe.maxDepth = -1
        arg_ihhe.bottomLeftValue = 0
        arg_ihhe.dfs(arg_xdvx, 0)
        return arg_ihhe.bottomLeftValue

    def func_rgwu(arg_ihhe, arg_wrnh: var_bacg, arg_osiz: var_hqta):
        if not arg_wrnh:
            return
        if arg_osiz > arg_ihhe.maxDepth:
            arg_ihhe.maxDepth = arg_osiz
            arg_ihhe.bottomLeftValue = arg_wrnh.val
        arg_ihhe.dfs(arg_wrnh.left, arg_osiz + 1)
        arg_ihhe.dfs(arg_wrnh.right, arg_osiz + 1)
        return
