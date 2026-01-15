class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = []
        var_hqta = []
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx) + 1):
            var_hqta.append(var_rgwu + 1)
            if var_rgwu == var_osiz(arg_xdvx) or arg_xdvx[var_rgwu] == 'I':
                while var_hqta:
                    var_bacg.append(var_rcsn(var_hqta.pop()))
        return ''.join(var_bacg)
