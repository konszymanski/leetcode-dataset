class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        if arg_xdvx == None or var_hqta(arg_xdvx) == 0:
            return ''
        for var_rgwu in var_wrnh(var_hqta(arg_xdvx[0])):
            var_osiz = arg_xdvx[0][var_rgwu]
            for var_ayzf in var_wrnh(1, var_hqta(arg_xdvx)):
                if var_rgwu == var_hqta(arg_xdvx[var_ayzf]) or arg_xdvx[
                    var_ayzf][var_rgwu] != var_osiz:
                    return arg_xdvx[0][0:var_rgwu]
        return arg_xdvx[0]
