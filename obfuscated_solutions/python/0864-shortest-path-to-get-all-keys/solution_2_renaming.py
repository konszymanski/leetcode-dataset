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

        def func_rjut(arg_lsgw):
            var_ayzf, var_wnki = var_wrnh[arg_lsgw]
            var_cbvh = [([False] * var_hqta) for var_yjch in var_dmio(var_bacg)
                ]
            var_cbvh[var_ayzf][var_wnki] = True
            var_ulfl = var_lgvi.deque([(var_ayzf, var_wnki, 0)])
            var_wvuc = {}
            while var_ulfl:
                var_ayzf, var_wnki, var_tufr = var_ulfl.popleft()
                if arg_lsgw != arg_rcsn[var_ayzf][var_wnki] != '.':
                    var_wvuc[arg_rcsn[var_ayzf][var_wnki]] = var_tufr
                    continue
                for var_zbxo, var_rdmc in func_llti(var_ayzf, var_wnki):
                    if arg_rcsn[var_zbxo][var_rdmc] != '#' and not var_cbvh[
                        var_zbxo][var_rdmc]:
                        var_cbvh[var_zbxo][var_rdmc] = True
                        var_ulfl.append((var_zbxo, var_rdmc, var_tufr + 1))
            return var_wvuc
        var_xhfo = {var_miuw: func_rjut(var_miuw) for var_miuw in var_wrnh}
        var_rhvk = 2 ** var_yybh(var_bzkm.islower() for var_bzkm in var_wrnh
            ) - 1
        var_icgs = [(0, '@', 0)]
        var_wkgu = var_lgvi.defaultdict(lambda : var_pmuo('inf'))
        var_wkgu['@', 0] = 0
        while var_icgs:
            var_tufr, var_miuw, var_eieh = var_xrri.heappop(var_icgs)
            if var_wkgu[var_miuw, var_eieh] < var_tufr:
                continue
            if var_eieh == var_rhvk:
                return var_tufr
            for var_xsns, var_mlhe in var_xhfo[var_miuw].iteritems():
                var_qpcy = var_eieh
                if var_xsns.islower():
                    var_qpcy |= 1 << var_bdeu(var_xsns) - var_bdeu('a')
                elif var_xsns.isupper():
                    if not var_eieh & 1 << var_bdeu(var_xsns) - var_bdeu('A'):
                        continue
                if var_tufr + var_mlhe < var_wkgu[var_xsns, var_qpcy]:
                    var_wkgu[var_xsns, var_qpcy] = var_tufr + var_mlhe
                    var_xrri.heappush(var_icgs, (var_tufr + var_mlhe,
                        var_xsns, var_qpcy))
        return -1
