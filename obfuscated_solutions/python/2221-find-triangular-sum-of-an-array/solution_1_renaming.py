class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        while var_hqta(arg_xdvx) > 1:
            var_rgwu = var_wrnh()
            for var_osiz in var_ayzf(var_hqta(arg_xdvx) - 1):
                var_rgwu.append((arg_xdvx[var_osiz] + arg_xdvx[var_osiz + 1
                    ]) % 10)
            arg_xdvx = var_rgwu
        return arg_xdvx[0]
