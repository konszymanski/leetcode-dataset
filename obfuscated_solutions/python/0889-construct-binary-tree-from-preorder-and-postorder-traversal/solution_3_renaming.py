class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.pre_index = 0
        arg_ihhe.post_index = 0

    def func_xdvx(arg_ihhe, arg_rcsn: var_hqta[var_rgwu], arg_bacg:
        var_hqta[var_rgwu]) ->var_wrnh[var_osiz]:
        return arg_ihhe._construct_tree(arg_rcsn, arg_bacg)

    def func_ayzf(arg_ihhe, arg_rcsn: var_hqta[var_rgwu], arg_bacg:
        var_hqta[var_rgwu]) ->var_wrnh[var_osiz]:
        var_wnki = var_osiz(arg_rcsn[arg_ihhe.pre_index])
        arg_ihhe.pre_index += 1
        if var_wnki.val != arg_bacg[arg_ihhe.post_index]:
            var_wnki.left = arg_ihhe._construct_tree(arg_rcsn, arg_bacg)
        if var_wnki.val != arg_bacg[arg_ihhe.post_index]:
            var_wnki.right = arg_ihhe._construct_tree(arg_rcsn, arg_bacg)
        arg_ihhe.post_index += 1
        return var_wnki
