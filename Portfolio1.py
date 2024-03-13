restaurants = [["Buddy's Pizza", "pizza", 4.6, 2], ["Bucharest Grill", "middle eastern", 4.2, 2], ["National Coney Island", "american", 4.1, 2], ["Morning Star Restaurant", 'american', 4.6, 1], ['Burger King', 'american', 3.2, 2], ["McDonald's", 'american', 2.9, 1], ['Del Taco', 'mexican', 3.9, 1]]


def greet():
    print("Hello, welcome to our restaurant reccomendation program!")

def goodbye():
    print("Thank you for using our service please consider using us again.")

def main():
    greet()
    search(list_categories())
    goodbye()

def search(seen):
    entry = input('Please enter an option: \n')
    search_data = {}
    for item in seen:
        count = 0
        for i in range(len(entry)):
            if item[i] == entry[i]:
                count += 1
            else:
                break
        search_data[item] = count
    if max(search_data.values()) == 0:
        print("That doesn't look like an option listed, please try again.")
        search(seen)
    else:
        category = max(search_data, key = lambda x: search_data[x])
        print(category)
        confirmation = input("You selected: " + category + '. Is this correct? Enter y/n.')
        if confirmation == 'y':
            results = get_results(category)
            print_results(results)
            search_again = input("Would you like to search again? y/n")
            if search_again == 'y':
                list_cats = input("Would you like to see the categories again? y/n")
                if list_cats == 'y':
                    search(list_categories())
                else:
                    search(seen)
                

        else:
            search(seen)

def get_results(category):
    result = []
    for restaurant in restaurants:
        if restaurant[1] == category:
            result.append(restaurant)
    return result

def print_results(results):
    for item in results:
        print('********************')
        print('Name:', item[0])
        print('Type:', item[1])
        print('Rating:', item[2])
        print('Price:', item[3])
        print('********************')

def list_categories():
    print("Please enter the type of restaurant you would like to search for, currently we have:")
    seen = []
    for restaurant in restaurants:
        if restaurant[1] not in seen:
            print(restaurant[1])
            seen.append(restaurant[1])
    return seen


if __name__ == '__main__':
    main()
