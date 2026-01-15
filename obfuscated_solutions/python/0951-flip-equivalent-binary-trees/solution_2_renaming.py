class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_hqta:
        if not arg_xdvx and not arg_rcsn:
            return True
        if arg_xdvx and arg_rcsn and arg_xdvx.val == arg_rcsn.val:
            return True
        return False

    def func_rgwu(arg_ihhe, arg_wrnh: var_bacg, arg_osiz: var_bacg) ->var_hqta:
        var_ayzf = []
        var_ayzf.append((arg_wrnh, arg_osiz))
        while var_ayzf:
            arg_xdvx, arg_rcsn = var_ayzf.pop()
            if not arg_xdvx and not arg_rcsn:
                continue
            if not arg_xdvx or not arg_rcsn:
                return False
            if arg_xdvx.val != arg_rcsn.val:
                return False
            if arg_ihhe.check_node_values(arg_xdvx.left, arg_rcsn.left
                ) and arg_ihhe.check_node_values(arg_xdvx.right, arg_rcsn.right
                ):
                var_ayzf.append((arg_xdvx.left, arg_rcsn.left))
                var_ayzf.append((arg_xdvx.right, arg_rcsn.right))
            elif arg_ihhe.check_node_values(arg_xdvx.left, arg_rcsn.right
                ) and arg_ihhe.check_node_values(arg_xdvx.right, arg_rcsn.left
                ):
                var_ayzf.append((arg_xdvx.left, arg_rcsn.right))
                var_ayzf.append((arg_xdvx.right, arg_rcsn.left))
            else:
                return False
        return True
