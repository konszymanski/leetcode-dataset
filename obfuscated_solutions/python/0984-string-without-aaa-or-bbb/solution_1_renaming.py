class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = []
        while arg_rcsn or arg_bacg:
            if var_rgwu(var_hqta) >= 2 and var_hqta[-1] == var_hqta[-2]:
                var_wrnh = var_hqta[-1] == 'b'
            else:
                var_wrnh = arg_rcsn >= arg_bacg
            if var_wrnh:
                arg_rcsn -= 1
                var_hqta.append('a')
            else:
                arg_bacg -= 1
                var_hqta.append('b')
        return ''.join(var_hqta)
