class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):

        def func_hqta(arg_rcsn):
            var_rgwu = []
            for var_wrnh in arg_rcsn:
                if var_wrnh != '#':
                    var_rgwu.append(var_wrnh)
                elif var_rgwu:
                    var_rgwu.pop()
            return ''.join(var_rgwu)
        return func_hqta(arg_rcsn) == func_hqta(arg_bacg)
