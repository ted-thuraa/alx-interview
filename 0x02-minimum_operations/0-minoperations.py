#!/usr/bin/python3
'''Minimum Operations
'''

def minOperations(n: int) -> int:
    '''Minimum operations needed to get H characters'''

    nextt = 'H'
    body = 'H'
    op_count = 0

    while (len(body)) < n:
        #current no of h divisible by n without remainder?
        if n % len(body) == 0:
            #if so means welldo copy all and paste
            op_count += 2
            nextt = body
            body += body
        else:
            #we only do paste what is in clipboard
            op_count += 1
            body += nextt
        if len(body) != n:
            return 0
        return op_count