class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu = var_hqta(0)
        var_wrnh = var_rgwu
        var_osiz = 0
        while arg_xdvx != None or arg_rcsn != None or var_osiz != 0:
            var_ayzf = arg_xdvx.val if arg_xdvx else 0
            var_wnki = arg_rcsn.val if arg_rcsn else 0
            var_egyk = var_ayzf + var_wnki + var_osiz
            var_osiz = var_egyk // 10
            var_dcmd = var_hqta(var_egyk % 10)
            var_wrnh.next = var_dcmd
            var_wrnh = var_dcmd
            arg_xdvx = arg_xdvx.next if arg_xdvx else None
            arg_rcsn = arg_rcsn.next if arg_rcsn else None
        return var_rgwu.next
