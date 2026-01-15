class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):

        def func_bacg(arg_hqta):
            var_rgwu = arg_hqta.right
            while var_rgwu.left is not None and var_rgwu.left is not arg_hqta:
                var_rgwu = var_rgwu.left
            return var_rgwu
        var_wrnh = 0
        arg_hqta = arg_rcsn
        while arg_hqta is not None:
            if arg_hqta.right is None:
                var_wrnh += arg_hqta.val
                arg_hqta.val = var_wrnh
                arg_hqta = arg_hqta.left
            else:
                var_rgwu = func_bacg(arg_hqta)
                if var_rgwu.left is None:
                    var_rgwu.left = arg_hqta
                    arg_hqta = arg_hqta.right
                else:
                    var_rgwu.left = None
                    var_wrnh += arg_hqta.val
                    arg_hqta.val = var_wrnh
                    arg_hqta = arg_hqta.left
        return arg_rcsn
