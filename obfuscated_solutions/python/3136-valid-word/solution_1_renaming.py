class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        if var_bacg(arg_xdvx) < 3:
            return False
        var_hqta = False
        var_rgwu = False
        for var_wrnh in arg_xdvx:
            if var_wrnh.isalpha():
                if var_wrnh.lower() in 'aeiou':
                    var_hqta = True
                else:
                    var_rgwu = True
            elif not var_wrnh.isdigit():
                return False
        return var_hqta and var_rgwu
