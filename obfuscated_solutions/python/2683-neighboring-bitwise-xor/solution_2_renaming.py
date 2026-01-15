class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_ayzf:
        var_hqta = [0]
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            var_hqta.append(arg_xdvx[var_rgwu] ^ var_hqta[var_rgwu])
        return var_hqta[0] == var_hqta[-1]
