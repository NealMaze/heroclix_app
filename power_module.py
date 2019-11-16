def perplex(subject, target, perplex_stat=move, perplex_value=0):
    perplex_stat = print('perplex what stat: ')
# LEFT OFF HERE #    perplex_value = print('perplex 
    if stat == move:
        curr.dial[0] = curr.dial[0] + perplex_value
    elif stat == attack:
        # I think that the stat values are actually the even [#]'s in the list,
        # the power values I think are the even 'indexes'?...
        # these list 'indexes'? need to moved to the evens
        curr.dial[1] = curr.dial[1] + perplex_value
    elif stat == defense:
        curr.dial[2] = curr.dial[2] + perplex_value
    elif stat == defense:
        curr.dial[3] = curr.dial[3] + perplex_value
    elif stat == defense:
        curr.dial[4] = curr.dial[4] + perplex_value
    else:
        print('invalid tarkget or value')


