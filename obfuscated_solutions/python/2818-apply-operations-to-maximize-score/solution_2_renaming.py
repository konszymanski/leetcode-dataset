class Solution:
    var_udax = var_ihhe(1000000000.0 + 7)

    def func_xdvx(arg_rcsn, arg_bacg: var_rgwu[var_ihhe], arg_hqta: var_ihhe
        ) ->var_ihhe:
        var_wrnh = var_osiz(arg_bacg)
        var_ayzf = [0] * var_wrnh
        var_wnki = var_egyk(arg_bacg)
        var_dcmd = arg_rcsn.get_primes(var_wnki)
        for var_llti in var_zbxo(var_wrnh):
            var_rdmc = arg_bacg[var_llti]
            for var_rjut in var_dcmd:
                if var_rjut * var_rjut > var_rdmc:
                    break
                if var_rdmc % var_rjut != 0:
                    continue
                var_ayzf[var_llti] += 1
                while var_rdmc % var_rjut == 0:
                    var_rdmc //= var_rjut
            if var_rdmc > 1:
                var_ayzf[var_llti] += 1
        var_lsgw = [var_wrnh] * var_wrnh
        var_cbvh = [-1] * var_wrnh
        var_yjch = var_dmio()
        for var_llti in var_zbxo(var_wrnh):
            while var_yjch and var_ayzf[var_yjch[-1]] < var_ayzf[var_llti]:
                var_ulfl = var_yjch.pop()
                var_lsgw[var_ulfl] = var_llti
            if var_yjch:
                var_cbvh[var_llti] = var_yjch[-1]
            var_yjch.append(var_llti)
        var_lgvi = [((var_lsgw[var_wvuc] - var_wvuc) * (var_wvuc - var_cbvh
            [var_wvuc])) for var_wvuc in var_zbxo(var_wrnh)]
        var_tufr = var_xhfo(var_miuw(arg_bacg), key=lambda x: -var_rhvk[1])
        var_yybh = 1

        def func_bzkm(arg_icgs, arg_wkgu):
            var_pmuo = 1
            while arg_wkgu > 0:
                if arg_wkgu % 2:
                    var_pmuo = var_pmuo * arg_icgs % arg_rcsn.MOD
                arg_icgs = arg_icgs * arg_icgs % arg_rcsn.MOD
                arg_wkgu //= 2
            return var_pmuo
        var_eieh = 0
        while arg_hqta > 0:
            var_llti, var_rdmc = var_tufr[var_eieh]
            var_eieh += 1
            var_xrri = var_xsns(arg_hqta, var_lgvi[var_llti])
            var_yybh = var_yybh * func_bzkm(var_rdmc, var_xrri) % arg_rcsn.MOD
            arg_hqta -= var_xrri
        return var_yybh

    def func_mlhe(arg_rcsn, arg_qpcy: var_ihhe) ->var_rgwu[var_ihhe]:
        var_bdeu = [True] * (arg_qpcy + 1)
        var_dcmd = []
        for var_fzvn in var_zbxo(2, arg_qpcy + 1):
            if not var_bdeu[var_fzvn]:
                continue
            var_dcmd.append(var_fzvn)
            for var_tcmm in var_zbxo(var_fzvn * var_fzvn, arg_qpcy + 1,
                var_fzvn):
                var_bdeu[var_tcmm] = False
        return var_dcmd
