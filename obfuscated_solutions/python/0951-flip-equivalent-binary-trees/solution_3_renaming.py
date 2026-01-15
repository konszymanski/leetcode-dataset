class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->None:
        if not arg_xdvx:
            return
        arg_ihhe.find_canonical_form(arg_xdvx.left)
        arg_ihhe.find_canonical_form(arg_xdvx.right)
        if not arg_xdvx.right:
            return
        if not arg_xdvx.left:
            arg_xdvx.left = arg_xdvx.right
            arg_xdvx.right = None
            return
        var_bacg = arg_xdvx.left
        var_hqta = arg_xdvx.right
        if var_bacg.val > var_hqta.val:
            arg_xdvx.left, arg_xdvx.right = arg_xdvx.right, arg_xdvx.left

    def func_rgwu(arg_ihhe, arg_wrnh: var_rcsn, arg_osiz: var_rcsn) ->var_ayzf:
        if not arg_wrnh and not arg_osiz:
            return True
        if not arg_wrnh or not arg_osiz:
            return False
        if arg_wrnh.val != arg_osiz.val:
            return False
        return arg_ihhe.are_equivalent(arg_wrnh.left, arg_osiz.left
            ) and arg_ihhe.are_equivalent(arg_wrnh.right, arg_osiz.right)

    def func_wnki(arg_ihhe, arg_wrnh: var_rcsn, arg_osiz: var_rcsn) ->var_ayzf:
        arg_ihhe.find_canonical_form(arg_wrnh)
        arg_ihhe.find_canonical_form(arg_osiz)
        return arg_ihhe.are_equivalent(arg_wrnh, arg_osiz)
