class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = None
        var_rgwu = None
        while arg_xdvx:
            var_rgwu = arg_xdvx.next
            arg_xdvx.next = var_hqta
            var_hqta = arg_xdvx
            arg_xdvx = var_rgwu
        return var_hqta

    def func_wrnh(arg_ihhe, arg_osiz: var_rcsn[var_bacg], arg_ayzf:
        var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_wnki = arg_ihhe.reverseList(arg_osiz)
        var_egyk = arg_ihhe.reverseList(arg_ayzf)
        var_dcmd = 0
        var_llti = 0
        var_zbxo = var_bacg()
        while var_wnki or var_egyk:
            if var_wnki:
                var_dcmd += var_wnki.val
                var_wnki = var_wnki.next
            if var_egyk:
                var_dcmd += var_egyk.val
                var_egyk = var_egyk.next
            var_zbxo.val = var_dcmd % 10
            var_llti = var_dcmd // 10
            arg_xdvx = var_bacg(var_llti)
            arg_xdvx.next = var_zbxo
            var_zbxo = arg_xdvx
            var_dcmd = var_llti
        return var_zbxo.next if var_llti == 0 else var_zbxo
