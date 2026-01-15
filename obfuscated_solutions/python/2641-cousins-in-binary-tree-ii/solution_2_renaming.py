class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.level_sums = [0] * 100000

    def func_xdvx(arg_ihhe, arg_rcsn):
        arg_ihhe._calculate_level_sum(arg_rcsn, 0)
        arg_ihhe.replace_value_in_tree_internal(arg_rcsn, 0, 0)
        return arg_rcsn

    def func_bacg(arg_ihhe, arg_hqta, arg_rgwu):
        if arg_hqta is None:
            return
        arg_ihhe.level_sums[arg_rgwu] += arg_hqta.val
        arg_ihhe._calculate_level_sum(arg_hqta.left, arg_rgwu + 1)
        arg_ihhe._calculate_level_sum(arg_hqta.right, arg_rgwu + 1)

    def func_wrnh(arg_ihhe, arg_hqta, arg_osiz, arg_rgwu):
        if arg_hqta is None:
            return
        var_ayzf = 0 if arg_hqta.left is None else arg_hqta.left.val
        var_wnki = 0 if arg_hqta.right is None else arg_hqta.right.val
        if arg_rgwu == 0 or arg_rgwu == 1:
            arg_hqta.val = 0
        else:
            arg_hqta.val = arg_ihhe.level_sums[arg_rgwu
                ] - arg_hqta.val - arg_osiz
        arg_ihhe.replace_value_in_tree_internal(arg_hqta.left, var_wnki, 
            arg_rgwu + 1)
        arg_ihhe.replace_value_in_tree_internal(arg_hqta.right, var_ayzf, 
            arg_rgwu + 1)
