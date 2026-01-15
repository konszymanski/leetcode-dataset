class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        var_hqta = var_rgwu([(0, 0)])
        var_wrnh = []
        while var_hqta:
            var_osiz, var_ayzf = var_hqta.popleft()
            var_wrnh.append(arg_xdvx[var_osiz][var_ayzf])
            if var_ayzf == 0 and var_osiz + 1 < var_wnki(arg_xdvx):
                var_hqta.append((var_osiz + 1, var_ayzf))
            if var_ayzf + 1 < var_wnki(arg_xdvx[var_osiz]):
                var_hqta.append((var_osiz, var_ayzf + 1))
        return var_wrnh
