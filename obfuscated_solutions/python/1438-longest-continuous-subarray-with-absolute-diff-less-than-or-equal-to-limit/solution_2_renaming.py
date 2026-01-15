from sortedcontainers import SortedDict


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh()
        var_osiz = 0
        var_ayzf = 0
        for var_wnki in var_egyk(var_dcmd(arg_xdvx)):
            if arg_xdvx[var_wnki] in var_rgwu:
                var_rgwu[arg_xdvx[var_wnki]] += 1
            else:
                var_rgwu[arg_xdvx[var_wnki]] = 1
            while var_rgwu.peekitem(-1)[0] - var_rgwu.peekitem(0)[0
                ] > arg_rcsn:
                var_rgwu[arg_xdvx[var_osiz]] -= 1
                if var_rgwu[arg_xdvx[var_osiz]] == 0:
                    var_rgwu.pop(arg_xdvx[var_osiz])
                var_osiz += 1
            var_ayzf = var_llti(var_ayzf, var_wnki - var_osiz + 1)
        return var_ayzf
