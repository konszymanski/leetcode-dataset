from collections import defaultdict
from random import choice


class RandomizedCollection:

    def func_udax(arg_ihhe):
        """
        Initialize your data structure here.
        """
        arg_ihhe.lst = []
        arg_ihhe.idx = var_xdvx(var_rcsn)

    def func_bacg(arg_ihhe, arg_hqta: var_rgwu) ->var_osiz:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        arg_ihhe.idx[arg_hqta].add(var_wrnh(arg_ihhe.lst))
        arg_ihhe.lst.append(arg_hqta)
        return var_wrnh(arg_ihhe.idx[arg_hqta]) == 1

    def func_ayzf(arg_ihhe, arg_hqta: var_rgwu) ->var_osiz:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not arg_ihhe.idx[arg_hqta]:
            return False
        func_ayzf, var_wnki = arg_ihhe.idx[arg_hqta].pop(), arg_ihhe.lst[-1]
        arg_ihhe.lst[func_ayzf] = var_wnki
        arg_ihhe.idx[var_wnki].add(func_ayzf)
        arg_ihhe.idx[var_wnki].discard(var_wrnh(arg_ihhe.lst) - 1)
        arg_ihhe.lst.pop()
        return True

    def func_egyk(arg_ihhe) ->var_rgwu:
        """
        Get a random element from the collection.
        """
        return var_dcmd(arg_ihhe.lst)
