class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_osiz:
        var_hqta = [arg_xdvx]
        var_rgwu = {}
        while var_hqta:
            var_wrnh = var_hqta[-1]
            if not var_wrnh.left and not var_wrnh.right:
                var_hqta.pop()
                var_rgwu[var_wrnh] = var_wrnh.val == 1
                continue
            if var_wrnh.left in var_rgwu and var_wrnh.right in var_rgwu:
                var_hqta.pop()
                if var_wrnh.val == 2:
                    var_rgwu[var_wrnh] = var_rgwu[var_wrnh.left] or var_rgwu[
                        var_wrnh.right]
                else:
                    var_rgwu[var_wrnh] = var_rgwu[var_wrnh.left] and var_rgwu[
                        var_wrnh.right]
            else:
                if var_wrnh.left:
                    var_hqta.append(var_wrnh.left)
                if var_wrnh.right:
                    var_hqta.append(var_wrnh.right)
        return var_rgwu[arg_xdvx]
