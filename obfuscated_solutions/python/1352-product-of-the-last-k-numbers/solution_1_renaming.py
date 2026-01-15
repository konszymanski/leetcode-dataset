class ProductOfNumbers:

    def func_udax(arg_ihhe):
        arg_ihhe.prefix_product = [1]
        arg_ihhe.size = 0

    def func_xdvx(arg_ihhe, arg_rcsn: var_bacg):
        if arg_rcsn == 0:
            arg_ihhe.prefix_product = [1]
            arg_ihhe.size = 0
        else:
            arg_ihhe.prefix_product.append(arg_ihhe.prefix_product[arg_ihhe
                .size] * arg_rcsn)
            arg_ihhe.size += 1

    def func_hqta(arg_ihhe, arg_rgwu: var_bacg) ->var_bacg:
        if arg_rgwu > arg_ihhe.size:
            return 0
        return arg_ihhe.prefix_product[arg_ihhe.size
            ] // arg_ihhe.prefix_product[arg_ihhe.size - arg_rgwu]
