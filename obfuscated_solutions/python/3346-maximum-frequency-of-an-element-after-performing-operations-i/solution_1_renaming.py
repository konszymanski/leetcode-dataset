class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        arg_xdvx.sort()
        var_wrnh = 0
        var_osiz = {}
        var_ayzf = 0
        for var_wnki in var_egyk(var_dcmd(arg_xdvx)):
            if arg_xdvx[var_wnki] != arg_xdvx[var_ayzf]:
                var_osiz[arg_xdvx[var_ayzf]] = var_wnki - var_ayzf
                var_wrnh = var_llti(var_wrnh, var_wnki - var_ayzf)
                var_ayzf = var_wnki
        var_osiz[arg_xdvx[var_ayzf]] = var_dcmd(arg_xdvx) - var_ayzf
        var_wrnh = var_llti(var_wrnh, var_dcmd(arg_xdvx) - var_ayzf)
        for var_wnki in var_egyk(arg_xdvx[0], arg_xdvx[-1] + 1):
            var_zbxo = var_rdmc.bisect_left(arg_xdvx, var_wnki - arg_rcsn)
            var_rjut = var_rdmc.bisect_right(arg_xdvx, var_wnki + arg_rcsn) - 1
            if var_wnki in var_osiz:
                var_lsgw = var_cbvh(var_rjut - var_zbxo + 1, var_osiz[
                    var_wnki] + arg_bacg)
            else:
                var_lsgw = var_cbvh(var_rjut - var_zbxo + 1, arg_bacg)
            var_wrnh = var_llti(var_wrnh, var_lsgw)
        return var_wrnh
