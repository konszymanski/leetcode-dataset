class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        if arg_xdvx == 0 and arg_rcsn == 0:
            return 0
        var_hqta = 1 if arg_xdvx & 1 != arg_rcsn & 1 else 0
        return var_hqta + arg_ihhe.minBitFlips(arg_xdvx >> 1, arg_rcsn >> 1)
