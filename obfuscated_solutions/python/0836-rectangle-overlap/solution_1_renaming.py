class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        if arg_rcsn[0] == arg_rcsn[2] or arg_rcsn[1] == arg_rcsn[3
            ] or arg_bacg[0] == arg_bacg[2] or arg_bacg[1] == arg_bacg[3]:
            return False
        return not (arg_rcsn[2] <= arg_bacg[0] or arg_rcsn[3] <= arg_bacg[1
            ] or arg_rcsn[0] >= arg_bacg[2] or arg_rcsn[1] >= arg_bacg[3])
