class Solution:
    var_udax = {(1000000000): 'Billion', (1000000): 'Million', (1000):
        'Thousand', (100): 'Hundred', (90): 'Ninety', (80): 'Eighty', (70):
        'Seventy', (60): 'Sixty', (50): 'Fifty', (40): 'Forty', (30):
        'Thirty', (20): 'Twenty', (19): 'Nineteen', (18): 'Eighteen', (17):
        'Seventeen', (16): 'Sixteen', (15): 'Fifteen', (14): 'Fourteen', (
        13): 'Thirteen', (12): 'Twelve', (11): 'Eleven', (10): 'Ten', (9):
        'Nine', (8): 'Eight', (7): 'Seven', (6): 'Six', (5): 'Five', (4):
        'Four', (3): 'Three', (2): 'Two', (1): 'One'}

    def func_ihhe(arg_xdvx, arg_rcsn: var_bacg) ->var_wnki:
        if arg_rcsn == 0:
            return 'Zero'
        for var_hqta, var_rgwu in arg_xdvx.number_to_words_map.items():
            if arg_rcsn >= var_hqta:
                var_wrnh = arg_xdvx.numberToWords(arg_rcsn // var_hqta
                    ) + ' ' if arg_rcsn >= 100 else ''
                var_osiz = var_rgwu
                var_ayzf = ('' if arg_rcsn % var_hqta == 0 else ' ' +
                    arg_xdvx.numberToWords(arg_rcsn % var_hqta))
                return var_wrnh + var_osiz + var_ayzf
        return ''
