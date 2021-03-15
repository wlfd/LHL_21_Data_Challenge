lease = '''Dear Dot, 
           This document validates that you are beholden to a monthly payment of rent for this house.
           Rent is to be paid by the first of every month.
           Fill in your signature to agree to these terms.  
            -------------
            Please Sign Here: 
'''
signature = 'Wilfred Lai'
new_lease = lease + signature  # valid, signature on next line
# new_lease = f'{lease}{signature}' # valid, same as above
# new_lease = f'{lease} + {signature}' # not valid, has '+' before name

print(new_lease)