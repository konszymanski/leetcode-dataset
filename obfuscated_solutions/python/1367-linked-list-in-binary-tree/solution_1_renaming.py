class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_rgwu]) ->var_wrnh:
        if arg_rcsn is None:
            return False
        return arg_ihhe._check_path(arg_rcsn, arg_xdvx)

    def func_osiz(arg_ihhe, arg_ayzf: var_bacg[var_rgwu], arg_xdvx:
        var_bacg[var_hqta]) ->var_wrnh:
        if arg_ayzf is None:
            return False
        if arg_ihhe._dfs(arg_ayzf, arg_xdvx):
            return True
        return arg_ihhe._check_path(arg_ayzf.left, arg_xdvx
            ) or arg_ihhe._check_path(arg_ayzf.right, arg_xdvx)

    def func_wnki(arg_ihhe, arg_ayzf: var_bacg[var_rgwu], arg_xdvx:
        var_bacg[var_hqta]) ->var_wrnh:
        if arg_xdvx is None:
            return True
        if arg_ayzf is None:
            return False
        if arg_ayzf.val != arg_xdvx.val:
            return False
        return arg_ihhe._dfs(arg_ayzf.left, arg_xdvx.next) or arg_ihhe._dfs(
            arg_ayzf.right, arg_xdvx.next)
