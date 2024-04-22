from views.OwnerView import owner_main
import sys
from views.WelcomeView import welcome

if __name__ == '__main__':
    if len(sys.argv) < 2:
        welcome()
    if sys.argv[1] == 'owner':
        owner_main()
    welcome()
