from views.OwnerView import owner_main
import sys
from views.WelcomeView import welcome

class Main:
    def main(self):
        welcome()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        Main.main()
    if sys.argv[1] == 'owner':
        owner_main()
    Main.main()
