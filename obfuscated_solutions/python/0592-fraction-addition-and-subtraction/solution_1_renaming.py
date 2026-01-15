class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = 0
        var_bacg = 1
        var_hqta = 0
        while var_hqta < var_rgwu(arg_xdvx):
            var_wrnh = 0
            var_osiz = 0
            var_ayzf = False
            if arg_xdvx[var_hqta] == '-' or arg_xdvx[var_hqta] == '+':
                if arg_xdvx[var_hqta] == '-':
                    var_ayzf = True
                var_hqta += 1
            while var_hqta < var_rgwu(arg_xdvx) and arg_xdvx[var_hqta].isdigit(
                ):
                var_wnki = var_egyk(arg_xdvx[var_hqta])
                var_wrnh = var_wrnh * 10 + var_wnki
                var_hqta += 1
            if var_ayzf:
                var_wrnh *= -1
            var_hqta += 1
            while var_hqta < var_rgwu(arg_xdvx) and arg_xdvx[var_hqta].isdigit(
                ):
                var_wnki = var_egyk(arg_xdvx[var_hqta])
                var_osiz = var_osiz * 10 + var_wnki
                var_hqta += 1
            var_rcsn = var_rcsn * var_osiz + var_wrnh * var_bacg
            var_bacg = var_bacg * var_osiz
        var_dcmd = var_llti(arg_ihhe._find_gcd(var_rcsn, var_bacg))
        var_rcsn //= var_dcmd
        var_bacg //= var_dcmd
        return f'{var_rcsn}/{var_bacg}'

    def func_zbxo(arg_ihhe, arg_rdmc, arg_rjut):
        if arg_rdmc == 0:
            return arg_rjut
        return arg_ihhe._find_gcd(arg_rjut % arg_rdmc, arg_rdmc)
