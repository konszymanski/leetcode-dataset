class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rgwu:
        if not var_hqta(arg_xdvx):
            return '0'


        class LargerStrComparator(var_rgwu):

            def func_wrnh(arg_ihhe, arg_osiz):
                return arg_ihhe + arg_osiz > arg_osiz + arg_ihhe
        var_ayzf = []
        for var_wnki in arg_xdvx:
            var_egyk.heappush(var_ayzf, var_dcmd(var_rgwu(var_wnki)))
        var_llti = []
        while var_ayzf:
            var_llti.append(var_egyk.heappop(var_ayzf))
        var_zbxo = ''.join(var_llti)
        return '0' if var_zbxo[0] == '0' else var_zbxo
