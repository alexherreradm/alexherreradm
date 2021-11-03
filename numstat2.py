#CALCULATE STATISTICS OF NUMBERS IN A TXT FILE


def do_stats():
    filename = input("What is the name of your file? ")
    num = 0
    try:
        infile = open(filename, 'r')
        count = 0
        total = 0.0
        average = 0.0
        maximum = 0
        minimum = 0
        range = 0
        for line in infile:
            num = int(line)
            count = count + 1
            total = total + num

            if count == 1:
                maximum = num
                minimum = num
            else:
                if num > maximum:
                    maximum = num
                if num < minimum:
                    minimum = num

        if count <= 0:
            print("There are no numbers in ", filename)
        else:
            if count > 0:
                average = total / count
                range = maximum - minimum

            print('File name: ', filename)
            print('Sum: ', total)
            print('Count: ', count)
            print('Average: ', average)
            print('Max: ', maximum)
            print('Min: ', minimum)
            print('Range: ', range)
        infile.close()
    except:
        print('File is not found. Try again.')


def main():
    while True:
        do_stats()
        response = input("Would you like to perform another calculation (y/n)? ")
        if (response == "y"):
            print("")
            continue
        else:
            break

main()