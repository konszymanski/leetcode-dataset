class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg, var_hqta = var_rgwu(arg_rcsn), var_rgwu(arg_rcsn[0])
        var_wrnh = {var_osiz: (var_ayzf, var_wnki) for var_ayzf, var_egyk in
            var_dcmd(arg_rcsn) for var_wnki, var_osiz in var_dcmd(var_egyk) if
            var_osiz not in '.#'}

        def func_llti(var_ayzf, var_wnki):
            for var_zbxo, var_rdmc in ((var_ayzf - 1, var_wnki), (var_ayzf,
                var_wnki - 1), (var_ayzf + 1, var_wnki), (var_ayzf, 
                var_wnki + 1)):
                if 0 <= var_zbxo < var_bacg and 0 <= var_rdmc < var_hqta:
                    yield var_zbxo, var_rdmc

        def func_rjut(arg_lsgw, arg_cbvh, arg_yjch=()):
            var_dmio, var_ulfl = var_wrnh[arg_lsgw]
            var_lgvi, var_wvuc = var_wrnh[arg_cbvh]
            var_tufr = [([False] * var_hqta) for var_xhfo in var_miuw(var_bacg)
                ]
            var_tufr[var_dmio][var_ulfl] = True
            var_rhvk = var_yybh.deque([(var_dmio, var_ulfl, 0)])
            while var_rhvk:
                var_ayzf, var_wnki, var_bzkm = var_rhvk.popleft()
                if var_ayzf == var_lgvi and var_wnki == var_wvuc:
                    return var_bzkm
                for var_zbxo, var_rdmc in func_llti(var_ayzf, var_wnki):
                    if not var_tufr[var_zbxo][var_rdmc] and arg_rcsn[var_zbxo][
                        var_rdmc] != '#':
                        if arg_rcsn[var_zbxo][var_rdmc].isupper() and arg_rcsn[
                            var_zbxo][var_rdmc].lower() not in keys:
                            continue
                        var_rhvk.append((var_zbxo, var_rdmc, var_bzkm + 1))
                        var_tufr[var_zbxo][var_rdmc] = True
            return var_icgs('inf')
        var_wkgu = var_icgs('inf')
        keys = ''.join(var_pmuo(var_eieh('a') + var_xrri) for var_xrri in
            var_miuw(var_rgwu(var_wrnh) / 2))
        for var_xsns in var_mlhe.permutations(keys):
            var_qpcy = 0
            for var_xrri, arg_cbvh in var_dcmd(var_xsns):
                arg_lsgw = var_xsns[var_xrri - 1] if var_xrri > 0 else '@'
                var_bzkm = func_rjut(arg_lsgw, arg_cbvh, var_xsns[:var_xrri])
                var_qpcy += var_bzkm
                if var_qpcy >= var_wkgu:
                    break
            else:
                var_wkgu = var_qpcy
        return var_wkgu if var_wkgu < var_icgs('inf') else -1
