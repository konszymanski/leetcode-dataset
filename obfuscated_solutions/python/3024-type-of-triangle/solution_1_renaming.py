class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_hqta:
        arg_xdvx.sort()
        if arg_xdvx[0] + arg_xdvx[1] <= arg_xdvx[2]:
            return 'none'
        elif arg_xdvx[0] == arg_xdvx[2]:
            return 'equilateral'
        elif arg_xdvx[0] == arg_xdvx[1] or arg_xdvx[1] == arg_xdvx[2]:
            return 'isosceles'
        else:
            return 'scalene'
