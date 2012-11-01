"""
try except test

"""


def main():
    try:
        import termios, TERMIOS
    except ImportError:
        try:
            import msvcrt
        except ImportError:
            try:
                import re
            except ImportError:
                print "we are here easydialogs"
            else:
                print "we are here 4"
                 
        else:
            print "we are here 3"
    else:
        print "we are here 2"

if __name__=="__main__":
    main()
