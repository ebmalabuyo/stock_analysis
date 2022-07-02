# Elijah Malabuyo

# imported matplotlib
import matplotlib.pyplot as plt


# the date of highest closing price and include price
def find_max_close(file):
    '''Takes a csv file as input and returns the highest closing price and its date'''
    ...
    try:
        # opens file and reads first line
        file = open(file, "r")
        file.readline()
        # reads second line and splits into lst
        second_line = file.readline()
        new = second_line.split(",")
        # converts lst values to int/float
        conv = [float("".join(x.replace('"', '').split(","))) for x in new[1:]]
        # first value is max
        max_val = conv[1]

        # parse through rest of lines in file and split the same way we did it above
        for line in file:
            s = line.split(",")
            float_lst = [float("".join(x.replace('"', '').split(","))) for x in s[1:]]
        # check if value is greater than max if so then it becomes the new max
            if float_lst[3] > max_val:
                max_val = float_lst[3]
                date = s[0]
        # close file
        file.close()
        # return values 
        return ('Max: Date                  Price' + '\n'
                + f'     {date}' + '            ${0:,.2f}'.format(max_val))
    except FileNotFoundError:
        print('File could not be found.')


# the date of lowest opening price include price
def find_min_open(file):
    '''Takes the csv file as input and returns the lowest opening price and its date'''
    ...
    try:
        # opens file and reads first line
        file = open(file, "r")
        # reads second line and splits into lst
        file.readline()
        second_line = file.readline()
        new = second_line.split(",")
        # converts lst values to int/float
        conv = [float("".join(x.replace('"', '').split(","))) for x in new[1:]]
        # first value is min
        min = conv[1]

        # parse through rest of lines in file and split the same way we did it above
        for line in file:
            s = line.split(",")
            float_lst = [float("".join(x.replace('"', '').split(","))) for x in s[1:]]
        # check if value is less than min if so then it becomes the new max
            if float_lst[0] < min:
                min = float_lst[0]
                date = s[0]
        # close file 
        file.close()
        # return value
        return ('Min: Date                  Price' + '\n'
                + f'     {date}' + '            ${0:,.2f}'.format(min))
    except FileNotFoundError:
        print('File could not be found.')


# a listing of 10 high closing price dates 
def list_10_high(file):
    '''Takes the csv file and returns the 10 highest closing price and dates'''
    try:
        # open the file 
        file = open(file, "r")
        # read first line of header
        close_lst = []
        file.readline()
        # go through each line in  the file
        for lines in file:
            # split each line into a list
            s = lines.split(",")
            # remove quote and cast to float
            t = s[4].replace('"', '')
            t = float(t)
            # add to list of all prices
            close_lst.append((t, s[0]))
        # sort to get top 10 highest prices
        top = sorted(close_lst, reverse=True)[:10]
        # unzip tuple into list to access each item
        new = [list(t) for t in zip(*top)]
        # print title of display
        print('10 Highest closing prices and dates:')
        # for loop to print out the price and corresponding dates
        for i in range(len(top)):
            print('Price:  ${0:,.2f}'.format(new[0][i]) + f' Date: {new[1][i]} ')
    except FileNotFoundError:
        # exception to handles error
        print('File could not be found.')


# a listing of the 10 lowest closing price and dates 
def list_10_low(file):
    '''Takes the csv file and returns the 10 lowest opening price and dates'''
    try:
        # open the file
        file = open(file, "r")
        # read first line of header
        close_lst = []
        file.readline()
        # go through each line in  the file
        for lines in file:
            # split each line into a list
            s = lines.split(",")
            # remove quote and cast to float
            t = s[1].replace('"', '')
            # change to float
            t = float(t)
            # add as tuple to list of all prices
            close_lst.append((t, s[0]))
        # sort to get 10 lowest prices
        low = sorted(close_lst)[:10]
        # unzip tuple into two lists with price and dates
        new = [list(t) for t in zip(*low)]
        # print header of display
        print('10 lowest opening prices and dates:')
        # for loop to display formated price and dates
        for i in range(len(low)):
            print('Price:  ${0:,.2f}'.format(new[0][i]) + f' Date: {new[1][i]} ')
    except FileNotFoundError:
        # exception to handle error
        print('File could not be found.')


# avg opening price of each month
def avg_open_price(file):
    '''Takes the csv file as input and displays a chart of the opening price each month'''
    ...
    # opens file and reads first line
    try:
        file = open(file, "r")
        file.readline()
        # initializes lists for opening prices and counts of month instances
        open_list = [0]*12
        count_list = [0]*12
        # parse through lines in file
        for line in file:
            s = line.split(",") # split line by commas
            month = int(s[0][:2]) # converts date to month index
            open_price = float(s[1].replace('"', '')) # take open price from file
            open_list[month-1] += open_price # add open price to list 
            count_list[month-1] += 1 # increase count at month index
        # create new list of averages
        avg_list = []
        # iterate for length of list
        for x in range(len(open_list)):
            avg_list.append(open_list[x] / count_list[x]) # add averages to list
        # create list of months
        months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        # create line graph using lists of avg prices and months
        plt.plot(months,avg_list)
        # add title and axis labels to line graph
        plt.title('Average Opening Price for Each Month')
        plt.xlabel('Month')
        plt.ylabel('Average Opening Price')
        plt.xticks(rotation = 45)
        # create list of ticks
        new_ticks = []
        # iterate through list of current ticks
        for x in plt.gca().get_yticks():
            new_ticks.append('${:1.0f}'.format(x)) # add formatted current tick to list
        # set y axis ticks to formatted tick list
        plt.gca().set_yticklabels(new_ticks)
        # display line graph
        plt.show()
    except FileNotFoundError:
        print('File could not be found')


# average closing price of each month
def avg_close_price(file):
    '''Takes the csv file as input and displays a chart of the closing price each month'''
    ...
    # opens file and reads first line
    try:
        file = open(file, "r")
        file.readline()
        # initializes lists for opening prices and counts of month instances
        close_list = [0]*12
        count_list = [0]*12
        # parse through lines in file
        for line in file:
            s = line.split(",") # split line by commas
            month = int(s[0][:2]) # converts date to month index
            close_price = float(s[4].replace('"', '')) # take close price from file
            close_list[month-1] += close_price # add close price to list 
            count_list[month-1] += 1 # increase count at month index
        # create new list of averages
        avg_list = []
        # iterate for length of list
        for x in range(len(close_list)):
            avg_list.append(close_list[x] / count_list[x]) # add averages to list
        # create list of months
        months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        # create line graph using lists of avg prices and months
        plt.plot(months,avg_list)
        # add title and axis labels to line graph
        plt.title('Average Closing Price for Each Month')
        plt.xlabel('Month')
        plt.ylabel('Average Closing Price')
        plt.xticks(rotation = 45)
        # create list of ticks
        new_ticks = []
        # iterate through list of current ticks
        for x in plt.gca().get_yticks():
            new_ticks.append('${:1.0f}'.format(x)) # add formatted current tick to list
        # set y axis ticks to formatted tick list
        plt.gca().set_yticklabels(new_ticks)
        # display line graph
        plt.show()
    except FileNotFoundError:
        print('File could not be found')


def main():
    '''Main function to run all functions together'''
    print(find_max_close("data.csv"))
    print(find_min_open("data.csv"))
    list_10_high("data.csv")
    list_10_low("data.csv")
    avg_open_price("data.csv")
    avg_close_price("data.csv")


if __name__ == '__main__':
    main()