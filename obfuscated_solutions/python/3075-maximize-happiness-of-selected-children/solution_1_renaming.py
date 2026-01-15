class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        arg_xdvx.sort(reverse=True)
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in var_ayzf(arg_rcsn):
            var_rgwu += var_wnki(arg_xdvx[var_osiz] - var_wrnh, 0)
            var_wrnh += 1
        return var_rgwu
