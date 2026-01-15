class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_hqta:
        arg_ihhe.current_string = ''
        arg_ihhe.result = ''
        arg_ihhe.index_in_sorted_list = 0
        arg_ihhe.generate_happy_strings(arg_xdvx, arg_rcsn)
        return arg_ihhe.result

    def func_rgwu(arg_ihhe, arg_xdvx, arg_rcsn):
        if var_wrnh(arg_ihhe.current_string) == arg_xdvx:
            arg_ihhe.index_in_sorted_list += 1
            if arg_ihhe.index_in_sorted_list == arg_rcsn:
                arg_ihhe.result = arg_ihhe.current_string
            return
        for var_osiz in ['a', 'b', 'c']:
            if var_wrnh(arg_ihhe.current_string
                ) > 0 and arg_ihhe.current_string[-1] == var_osiz:
                continue
            arg_ihhe.current_string += var_osiz
            arg_ihhe.generate_happy_strings(arg_xdvx, arg_rcsn)
            if arg_ihhe.result != '':
                return
            arg_ihhe.current_string = arg_ihhe.current_string[:-1]
