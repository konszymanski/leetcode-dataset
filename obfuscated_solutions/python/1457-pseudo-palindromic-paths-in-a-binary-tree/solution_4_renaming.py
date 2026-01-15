class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = 0
        var_hqta = [(arg_xdvx, 0)]
        while var_hqta:
            var_rgwu, var_wrnh = var_hqta.pop()
            if var_rgwu is not None:
                var_wrnh = var_wrnh ^ 1 << var_rgwu.val
                if var_rgwu.left is None and var_rgwu.right is None:
                    if var_wrnh & var_wrnh - 1 == 0:
                        var_bacg += 1
                else:
                    var_hqta.append((var_rgwu.right, var_wrnh))
                    var_hqta.append((var_rgwu.left, var_wrnh))
        return var_bacg
