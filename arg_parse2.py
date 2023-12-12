import argparse
import sys


# def check_args(args=None):
#     parser = argparse.ArgumentParser(
#         description='Script to learn basic argparse'
#     )
#     parser.add_argument(
#         '-H', '--host',
#         help = 'host ip',
#         # required = True,
#         default = 'localhost'
#     )
#     parser.add_argument(
#         '-p', '--port',
#         help = 'port of the web server',
#         default = '8080'
#     )
#     parser.add_argument(
#         '-u', '--user',
#         help = 'user name', 
#         default = 'root'
#     )

#     results = parser.parse_args()
#     return (results.host, results.port, results.user)

# if __name__ == '__main__':
#     h, p, u = check_args(sys.argv[1:])
#     print('h = ', h)
#     print('p =', p)
#     print('u =', u)


def check_args(args=None):
    parser = argparse.ArgumentParser(
        description='Script to learn basic argparse'
    )
    parser.add_argument(
        '-H', '--host',
        help='host ip',
        default='localhost'
    )
    parser.add_argument(
        '-p','--port',  
        help='port',
        default='8080'
    )
    
    parser.add_argument(
        '-u','--user',
        help='user',
        default='root'
    )
    parser.add_argument(
        'filename', 
        help='filename'
    )

    results = parser.parse_args()
    return (results.host, results.port, results.user, results.filename)


if __name__ == '__main__':
    h, p, u, f = check_args(sys.argv[1:])
    print('h = ', h)
    print('p = ', p)
    print('u = ', u)

    if h:
        if f.endswith('.txt'):
            with open(f,'w') as file:
                file.write(h)
