import sys
import csv
from tabulate import tabulate

def main():
    check_file()
    data = sys.argv[1]
    create_menu(data)
    print(ending())

def check_file():
    if len(sys.argv) < 2:
        sys.exit("Input hdb.csv!")
    elif len(sys.argv) > 2:
        sys.exit("Too many files! Input hdb.csv only...")
    if ".csv" not in sys.argv[1]:
        sys.exit("Wrong file type! Input hdb.csv!")

def create_menu(data):
    #menu UX
    output = "\nWelcome to Singapore Home Buying Companion, please select an option!\n"
    output += "[1] : See neighbourhoods\n"
    output += "[2] : Select top n towns with cheapest housings(2023)\n"
    print(output)

    #going about the menu
    while True:
        try:
            n = int(input("select option: "))
            if n == 1:
                return see_neighbourhoods(data)
            elif n == 2:
                 return n_cheapest_housings_2023(data)
        except:
            print("Invalid input:")
            pass

def see_neighbourhoods(data):
        with open(data, "r") as csvfile:
            data = csv.DictReader(csvfile)
            town_list = []
            n = 0
            for row in data:
                if row["town"] not in town_list:
                    n += 1
                    town_list.append(row["town"])
                    initial = (str(n) + ")").replace(" ","")
                    print("\n")
                    print(initial, row["town"])

def n_cheapest_housings_2023(data):

    with open(data, "r") as csvfile:
            data = csv.DictReader(csvfile)
            town_list = []
            n = 0
            # print("\n")
            for row in data:
                if row["flat_type"] not in town_list:
                    n += 1
                    town_list.append(row["flat_type"])
                    initial = (str(n) + ")").replace(" ","")
                    print(initial, row["flat_type"])

            while True:
                try:
                    k = int(input("\nselect option: "))
                    if k in [1, 2, 3, 4]:
                        chosenType = town_list[k-1]
                        print("Flat Type:", chosenType)
                        topk = int(input("\nFilter to top ___ towns? "))
                        break
                    else:
                        raise Exception()
                except:
                    print("try again! ")
                    pass

            d = {}

            csvfile.seek(0)   #read again
            data = list(csv.reader(csvfile))
            data = data[1:]

            for year, quarter, town, flat_type, price in data:
                year, price = int(year), int(price)
                if town not in d:
                    d[town] = []
                if year == 2023 and flat_type == chosenType:
                    d[town].append(price)

            keys_to_delete = []
            for k, v in d.items():
                if len(v) == 0:
                    keys_to_delete.append(k)
                    d[k] = 0
                else:
                    d[k] = "$" + str(int(round((sum(v)/len(v)), -2)))

            for k in keys_to_delete:
                del d[k]

            sorted_towns = sorted(d.items(), key = lambda x : x[1])

            hi = True
            while hi:
                if sorted_towns[topk-1][1] == sorted_towns[topk][1]:
                    topk += 1
                else:
                    hi = False

            table = sorted_towns[:topk]
            indexes = []
            for i in range(0, len(table)):
                newList = [i+1]
                newList.extend(list(table[i]))
                indexes.append(newList)
            header = []
            header.extend(['', 'town', 'avg price in 2023'])
            print("\n", tabulate(indexes, headers = header, tablefmt = "grid"))

def ending():
    return "\nThanks for using, bye!"

if __name__ == "__main__":
    main()