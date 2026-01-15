class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_egyk[var_dcmd]:
        if not arg_xdvx:
            return []
        var_hqta = []
        var_rgwu = [(arg_xdvx, 0)]
        while var_rgwu:
            var_wrnh, var_osiz = var_rgwu.pop()
            if var_osiz == var_ayzf(var_hqta):
                var_hqta.append(var_wrnh.val)
            else:
                var_hqta[var_osiz] = var_wnki(var_hqta[var_osiz], var_wrnh.val)
            if var_wrnh.left:
                var_rgwu.append((var_wrnh.left, var_osiz + 1))
            if var_wrnh.right:
                var_rgwu.append((var_wrnh.right, var_osiz + 1))
        return var_hqta
