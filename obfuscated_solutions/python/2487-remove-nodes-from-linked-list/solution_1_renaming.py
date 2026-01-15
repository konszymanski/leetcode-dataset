class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = []
        var_rgwu = arg_xdvx
        while var_rgwu:
            var_hqta.append(var_rgwu)
            var_rgwu = var_rgwu.next
        var_rgwu = var_hqta.pop()
        var_wrnh = var_rgwu.val
        var_osiz = var_bacg(var_wrnh)
        while var_hqta:
            var_rgwu = var_hqta.pop()
            if var_rgwu.val < var_wrnh:
                continue
            else:
                var_ayzf = var_bacg(var_rgwu.val)
                var_ayzf.next = var_osiz
                var_osiz = var_ayzf
                var_wrnh = var_rgwu.val
        return var_osiz
