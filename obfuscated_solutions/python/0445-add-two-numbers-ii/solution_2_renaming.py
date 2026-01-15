class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu = []
        var_wrnh = []
        while arg_xdvx:
            var_rgwu.append(arg_xdvx.val)
            arg_xdvx = arg_xdvx.next
        while arg_rcsn:
            var_wrnh.append(arg_rcsn.val)
            arg_rcsn = arg_rcsn.next
        var_osiz = 0
        var_ayzf = 0
        var_wnki = var_hqta()
        while var_rgwu or var_wrnh:
            if var_rgwu:
                var_osiz += var_rgwu.pop()
            if var_wrnh:
                var_osiz += var_wrnh.pop()
            var_wnki.val = var_osiz % 10
            var_ayzf = var_osiz // 10
            var_egyk = var_hqta(var_ayzf)
            var_egyk.next = var_wnki
            var_wnki = var_egyk
            var_osiz = var_ayzf
        return var_wnki.next if var_ayzf == 0 else var_wnki
