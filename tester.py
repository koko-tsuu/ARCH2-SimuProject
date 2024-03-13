import main_helpers
import sub_helpers

def main():
    # need to handle negative (check if '-' at first pos)
    # bawal floating points ata for exponent?
    sBinary = sub_helpers.base10Move("2132", "-5")
    print(sBinary)

if __name__ == '__main__':
    main()