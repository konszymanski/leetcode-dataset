class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        arg_ihhe.result = []
        arg_ihhe.build_sequence(0, 0, arg_xdvx)
        return ''.join(arg_ihhe.result[::-1])

    def func_bacg(arg_ihhe, arg_hqta: var_wrnh, arg_rgwu: var_wrnh,
        arg_xdvx: var_rcsn) ->var_wrnh:
        if arg_hqta != var_osiz(arg_xdvx):
            if arg_xdvx[arg_hqta] == 'I':
                arg_ihhe.build_sequence(arg_hqta + 1, arg_hqta + 1, arg_xdvx)
            else:
                arg_rgwu = arg_ihhe.build_sequence(arg_hqta + 1, arg_rgwu,
                    arg_xdvx)
        arg_ihhe.result.append(var_rcsn(arg_rgwu + 1))
        return arg_rgwu + 1
