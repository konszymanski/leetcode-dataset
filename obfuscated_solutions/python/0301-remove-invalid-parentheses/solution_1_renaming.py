class Solution(var_udax):

    def func_ihhe(arg_xdvx):
        arg_xdvx.valid_expressions = None
        arg_xdvx.min_removed = None

    def func_rcsn(arg_xdvx):
        arg_xdvx.valid_expressions = var_bacg()
        arg_xdvx.min_removed = var_hqta('inf')
    """
        string: The original string we are recursing on.
        index: current index in the original string.
        left: number of left parentheses till now.
        right: number of right parentheses till now.
        ans: the resulting expression in this particular recursion.
        ignored: number of parentheses ignored in this particular recursion.
    """

    def func_rgwu(arg_xdvx, arg_wrnh, arg_osiz, arg_ayzf, arg_wnki,
        arg_egyk, arg_dcmd):
        if arg_osiz == var_llti(arg_wrnh):
            if arg_ayzf == arg_wnki:
                if arg_dcmd <= arg_xdvx.min_removed:
                    var_zbxo = ''.join(arg_egyk)
                    if arg_dcmd < arg_xdvx.min_removed:
                        arg_xdvx.valid_expressions = var_bacg()
                        arg_xdvx.min_removed = arg_dcmd
                    arg_xdvx.valid_expressions.add(var_zbxo)
        else:
            var_rdmc = arg_wrnh[arg_osiz]
            if var_rdmc != '(' and var_rdmc != ')':
                arg_egyk.append(var_rdmc)
                arg_xdvx.remaining(arg_wrnh, arg_osiz + 1, arg_ayzf,
                    arg_wnki, arg_egyk, arg_dcmd)
                arg_egyk.pop()
            else:
                arg_xdvx.remaining(arg_wrnh, arg_osiz + 1, arg_ayzf,
                    arg_wnki, arg_egyk, arg_dcmd + 1)
                arg_egyk.append(var_rdmc)
                if arg_wrnh[arg_osiz] == '(':
                    arg_xdvx.remaining(arg_wrnh, arg_osiz + 1, arg_ayzf + 1,
                        arg_wnki, arg_egyk, arg_dcmd)
                elif arg_wnki < arg_ayzf:
                    arg_xdvx.remaining(arg_wrnh, arg_osiz + 1, arg_ayzf, 
                        arg_wnki + 1, arg_egyk, arg_dcmd)
                arg_egyk.pop()

    def func_rjut(arg_xdvx, arg_lsgw):
        """
        :type s: str
        :rtype: List[str]
        """
        arg_xdvx.reset()
        arg_xdvx.remaining(arg_lsgw, 0, 0, 0, [], 0)
        return var_cbvh(arg_xdvx.valid_expressions)
