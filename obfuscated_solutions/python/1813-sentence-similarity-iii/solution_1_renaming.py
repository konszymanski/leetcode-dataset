class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_osiz:
        var_hqta = var_rgwu(arg_xdvx.split())
        var_wrnh = var_rgwu(arg_rcsn.split())
        while var_hqta and var_wrnh and var_hqta[0] == var_wrnh[0]:
            var_hqta.popleft()
            var_wrnh.popleft()
        while var_hqta and var_wrnh and var_hqta[-1] == var_wrnh[-1]:
            var_hqta.pop()
            var_wrnh.pop()
        return not var_hqta or not var_wrnh
