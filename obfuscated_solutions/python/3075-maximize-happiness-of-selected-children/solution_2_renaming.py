class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = [(-var_wrnh) for var_wrnh in arg_xdvx]
        var_osiz.heapify(var_rgwu)
        var_ayzf = 0
        var_wnki = 0
        for var_egyk in var_dcmd(arg_rcsn):
            var_ayzf += var_llti(-var_osiz.heappop(var_rgwu) - var_wnki, 0)
            var_wnki += 1
        return var_ayzf
