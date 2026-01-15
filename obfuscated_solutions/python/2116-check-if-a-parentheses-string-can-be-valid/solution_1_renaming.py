class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_xdvx)
        if var_bacg % 2 == 1:
            return False
        var_rgwu = []
        var_wrnh = []
        for var_osiz in var_ayzf(var_bacg):
            if arg_rcsn[var_osiz] == '0':
                var_wrnh.append(var_osiz)
            elif arg_xdvx[var_osiz] == '(':
                var_rgwu.append(var_osiz)
            elif arg_xdvx[var_osiz] == ')':
                if var_rgwu:
                    var_rgwu.pop()
                elif var_wrnh:
                    var_wrnh.pop()
                else:
                    return False
        while var_rgwu and var_wrnh and var_rgwu[-1] < var_wrnh[-1]:
            var_rgwu.pop()
            var_wrnh.pop()
        if var_rgwu:
            return False
        return True
