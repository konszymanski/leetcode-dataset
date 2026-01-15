class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf()
        var_wnki = []
        for var_egyk in var_dcmd(var_rgwu):
            var_wnki.append(arg_rcsn[var_rgwu - var_egyk - 1])
            var_osiz.append(arg_xdvx[var_egyk])
        var_llti = 0
        while var_wrnh(var_osiz) > 0 and var_llti < var_wrnh(var_osiz):
            if var_wnki[-1] == var_osiz[0]:
                var_wnki.pop()
                var_osiz.popleft()
                var_llti = 0
            else:
                var_osiz.append(var_osiz.popleft())
                var_llti += 1
        return var_wrnh(var_osiz)
