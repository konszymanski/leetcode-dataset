class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu()
        var_wrnh = var_rgwu()
        var_osiz = 0
        var_ayzf = 0
        for var_wnki, var_egyk in var_dcmd(arg_xdvx):
            while var_hqta and arg_xdvx[var_hqta[-1]] < var_egyk:
                var_hqta.pop()
            var_hqta.append(var_wnki)
            while var_wrnh and arg_xdvx[var_wrnh[-1]] > var_egyk:
                var_wrnh.pop()
            var_wrnh.append(var_wnki)
            while var_hqta and var_wrnh and arg_xdvx[var_hqta[0]] - arg_xdvx[
                var_wrnh[0]] > 2:
                if var_hqta[0] < var_wrnh[0]:
                    var_osiz = var_hqta[0] + 1
                    var_hqta.popleft()
                else:
                    var_osiz = var_wrnh[0] + 1
                    var_wrnh.popleft()
            var_ayzf += var_wnki - var_osiz + 1
        return var_ayzf
