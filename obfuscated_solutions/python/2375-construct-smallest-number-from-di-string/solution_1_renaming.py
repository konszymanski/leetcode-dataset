class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_osiz:
        for var_hqta in var_rgwu(var_wrnh(arg_rcsn)):
            if arg_rcsn[var_hqta] == 'I' and arg_xdvx[var_hqta] > arg_xdvx[
                var_hqta + 1]:
                return False
            elif arg_rcsn[var_hqta] == 'D' and arg_xdvx[var_hqta] < arg_xdvx[
                var_hqta + 1]:
                return False
        return True

    def func_ayzf(arg_ihhe, arg_rcsn: var_bacg) ->var_bacg:
        var_wnki = var_wrnh(arg_rcsn)
        arg_xdvx = ''.join(var_bacg(var_egyk) for var_egyk in var_rgwu(1, 
            var_wnki + 2))
        for var_dcmd in var_llti(arg_xdvx):
            var_zbxo = ''.join(var_dcmd)
            if arg_ihhe.check(var_zbxo, arg_rcsn):
                return var_zbxo
        return ''
