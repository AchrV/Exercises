user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper(args, **kwargs):
        print(args)
        if args['valid']:
            fn(args, **kwargs)
        else:
            print("not authorised")
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
