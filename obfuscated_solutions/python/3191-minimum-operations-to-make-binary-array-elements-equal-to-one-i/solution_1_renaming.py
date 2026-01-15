class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu()
        var_wrnh = 0
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            while var_hqta and var_osiz > var_hqta[0] + 2:
                var_hqta.popleft()
            if (arg_xdvx[var_osiz] + var_wnki(var_hqta)) % 2 == 0:
                if var_osiz + 2 >= var_wnki(arg_xdvx):
                    return -1
                var_wrnh += 1
                var_hqta.append(var_osiz)
        return var_wrnh
