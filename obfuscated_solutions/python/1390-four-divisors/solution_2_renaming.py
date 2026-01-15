class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta, var_rgwu = 100000, 46
        var_wrnh = [True] * (var_hqta + 1)
        var_osiz = var_ayzf()
        for var_wnki in var_egyk(2, var_hqta + 1):
            if var_wrnh[var_wnki]:
                var_osiz.append(var_wnki)
            for var_dcmd in var_egyk(var_wnki + var_wnki, var_hqta + 1,
                var_wnki):
                var_wrnh[var_dcmd] = False
        """
        for i in range(2, C + 1):
            if isprime[i]:
                primes.append(i)
            for prime in primes:
                if i * prime > C:
                    break
                isprime[i * prime] = False
                if i % prime == 0:
                    break
        """
        var_llti = var_zbxo()
        for var_rdmc in var_osiz:
            if var_rdmc <= var_rgwu:
                var_llti[var_rdmc ** 3
                    ] = 1 + var_rdmc + var_rdmc ** 2 + var_rdmc ** 3
        for var_wnki in var_egyk(var_rjut(var_osiz)):
            for var_dcmd in var_egyk(var_wnki + 1, var_rjut(var_osiz)):
                if var_osiz[var_wnki] * var_osiz[var_dcmd] <= var_hqta:
                    var_llti[var_osiz[var_wnki] * var_osiz[var_dcmd]
                        ] = 1 + var_osiz[var_wnki] + var_osiz[var_dcmd
                        ] + var_osiz[var_wnki] * var_osiz[var_dcmd]
                else:
                    break
        var_lsgw = 0
        for var_cbvh in arg_xdvx:
            if var_cbvh in var_llti:
                var_lsgw += var_llti[var_cbvh]
        return var_lsgw
