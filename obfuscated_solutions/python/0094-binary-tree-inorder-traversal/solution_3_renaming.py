class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh[var_osiz]:
        var_bacg = []
        var_hqta = arg_xdvx
        while var_hqta is not None:
            if var_hqta.left is None:
                var_bacg.append(var_hqta.val)
                var_hqta = var_hqta.right
            else:
                var_rgwu = var_hqta.left
                while (var_rgwu.right is not None and var_rgwu.right !=
                    var_hqta):
                    var_rgwu = var_rgwu.right
                if var_rgwu.right is None:
                    var_rgwu.right = var_hqta
                    var_hqta = var_hqta.left
                else:
                    var_rgwu.right = None
                    var_bacg.append(var_hqta.val)
                    var_hqta = var_hqta.right
        return var_bacg
