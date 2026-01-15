class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_llti:
        var_hqta = var_rgwu()
        var_wrnh = []
        var_wrnh.append(arg_xdvx)
        while var_wrnh:
            var_osiz = var_wrnh.pop(0)
            if var_osiz == arg_rcsn:
                return True
            for var_ayzf in var_wnki(1, var_egyk(var_osiz)):
                if var_osiz[var_ayzf] == 'L' and var_osiz[var_ayzf - 1] == '_':
                    var_osiz = var_dcmd(var_osiz)
                    var_osiz[var_ayzf], var_osiz[var_ayzf - 1] = var_osiz[
                        var_ayzf - 1], var_osiz[var_ayzf]
                    var_osiz = ''.join(var_osiz)
                    if var_osiz not in var_hqta:
                        var_wrnh.append(var_osiz)
                        var_hqta.add(var_osiz)
                    var_osiz = var_dcmd(var_osiz)
                    var_osiz[var_ayzf], var_osiz[var_ayzf - 1] = var_osiz[
                        var_ayzf - 1], var_osiz[var_ayzf]
                    var_osiz = ''.join(var_osiz)
                if var_ayzf < var_egyk(var_osiz) - 1 and var_osiz[var_ayzf
                    ] == 'R' and var_osiz[var_ayzf + 1] == '_':
                    var_osiz = var_dcmd(var_osiz)
                    var_osiz[var_ayzf], var_osiz[var_ayzf + 1] = var_osiz[
                        var_ayzf + 1], var_osiz[var_ayzf]
                    var_osiz = ''.join(var_osiz)
                    if var_osiz not in var_hqta:
                        var_wrnh.append(var_osiz)
                        var_hqta.add(var_osiz)
                    var_osiz = var_dcmd(var_osiz)
                    var_osiz[var_ayzf], var_osiz[var_ayzf + 1] = var_osiz[
                        var_ayzf + 1], var_osiz[var_ayzf]
                    var_osiz = ''.join(var_osiz)
        return False
