class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = []

        def func_hqta(arg_rgwu):
            if arg_rgwu:
                var_bacg.append(arg_rgwu.val)
                func_hqta(arg_rgwu.left)
                func_hqta(arg_rgwu.right)
        func_hqta(arg_rcsn)
        return var_wrnh(var_osiz(var_bacg)) == 1
