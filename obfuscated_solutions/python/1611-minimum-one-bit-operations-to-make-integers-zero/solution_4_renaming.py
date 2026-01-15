class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = arg_xdvx
        var_bacg ^= var_bacg >> 16
        var_bacg ^= var_bacg >> 8
        var_bacg ^= var_bacg >> 4
        var_bacg ^= var_bacg >> 2
        var_bacg ^= var_bacg >> 1
        return var_bacg
