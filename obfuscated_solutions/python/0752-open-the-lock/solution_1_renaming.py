class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_lgvi:
        var_rgwu = {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5':
            '6', '6': '7', '7': '8', '8': '9', '9': '0'}
        var_wrnh = {'0': '9', '1': '0', '2': '1', '3': '2', '4': '3', '5':
            '4', '6': '5', '7': '6', '8': '7', '9': '8'}
        var_osiz = var_ayzf(arg_xdvx)
        var_wnki = var_egyk()
        var_dcmd = 0
        if '0000' in var_osiz:
            return -1
        var_wnki.append('0000')
        var_osiz.add('0000')
        while var_wnki:
            var_llti = var_zbxo(var_wnki)
            for var_rdmc in var_rjut(var_llti):
                var_lsgw = var_wnki.popleft()
                if var_lsgw == arg_rcsn:
                    return var_dcmd
                for var_cbvh in var_rjut(4):
                    var_yjch = var_dmio(var_lsgw)
                    var_yjch[var_cbvh] = var_rgwu[var_yjch[var_cbvh]]
                    var_ulfl = ''.join(var_yjch)
                    if var_ulfl not in var_osiz:
                        var_wnki.append(var_ulfl)
                        var_osiz.add(var_ulfl)
                    var_yjch = var_dmio(var_lsgw)
                    var_yjch[var_cbvh] = var_wrnh[var_yjch[var_cbvh]]
                    var_ulfl = ''.join(var_yjch)
                    if var_ulfl not in var_osiz:
                        var_wnki.append(var_ulfl)
                        var_osiz.add(var_ulfl)
            var_dcmd += 1
        return -1
