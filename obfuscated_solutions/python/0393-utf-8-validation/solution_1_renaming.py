class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        """
        :type data: List[int]
        :rtype: bool
        """
        var_rcsn = 0
        for var_bacg in arg_xdvx:
            var_hqta = var_rgwu(var_bacg, '#010b')[-8:]
            if var_rcsn == 0:
                for var_wrnh in var_hqta:
                    if var_wrnh == '0':
                        break
                    var_rcsn += 1
                if var_rcsn == 0:
                    continue
                if var_rcsn == 1 or var_rcsn > 4:
                    return False
            elif not (var_hqta[0] == '1' and var_hqta[1] == '0'):
                return False
            var_rcsn -= 1
        return var_rcsn == 0
