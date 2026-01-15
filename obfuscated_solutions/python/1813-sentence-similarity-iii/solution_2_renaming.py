class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_egyk:
        var_hqta = arg_xdvx.split(' ')
        var_rgwu = arg_rcsn.split(' ')
        var_wrnh, var_osiz, var_ayzf = 0, var_wnki(var_hqta) - 1, var_wnki(
            var_rgwu) - 1
        if var_wnki(var_hqta) > var_wnki(var_rgwu):
            return arg_ihhe.areSentencesSimilar(arg_rcsn, arg_xdvx)
        while var_wrnh < var_wnki(var_hqta) and var_hqta[var_wrnh] == var_rgwu[
            var_wrnh]:
            var_wrnh += 1
        while var_osiz >= 0 and var_hqta[var_osiz] == var_rgwu[var_ayzf]:
            var_osiz -= 1
            var_ayzf -= 1
        return var_osiz < var_wrnh
