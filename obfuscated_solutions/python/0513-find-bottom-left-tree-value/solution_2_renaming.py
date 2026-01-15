class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg()
        var_hqta = arg_xdvx
        var_rcsn.append(var_hqta)
        while var_rcsn:
            var_hqta = var_rcsn.popleft()
            if var_hqta.right:
                var_rcsn.append(var_hqta.right)
            if var_hqta.left:
                var_rcsn.append(var_hqta.left)
        return var_hqta.val
