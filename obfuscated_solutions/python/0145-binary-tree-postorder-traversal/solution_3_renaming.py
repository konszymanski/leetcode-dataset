class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = []
        if arg_xdvx is None:
            return var_rcsn
        var_bacg = []
        var_hqta = []
        var_bacg.append(arg_xdvx)
        while var_bacg:
            arg_xdvx = var_bacg[-1]
            if var_hqta and var_hqta[-1] == arg_xdvx:
                var_rcsn.append(arg_xdvx.val)
                var_bacg.pop()
                var_hqta.pop()
            else:
                var_hqta.append(arg_xdvx)
                if arg_xdvx.right is not None:
                    var_bacg.append(arg_xdvx.right)
                if arg_xdvx.left is not None:
                    var_bacg.append(arg_xdvx.left)
        return var_rcsn
