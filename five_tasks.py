''' five tasks
    (c)CyberNetRunner
'''

# lists
numbers = [1, 2, 4, 5, 4, 34, 65, 6, 100]
numbers_two = [1, 2, 3, 4, 5]
letters = ["a", "b", "c", "d", "e"]


# algorithms
def BubbleSortByFirstDigit(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            jx = str(arr[j])
            jz = str(arr[j+1])
            if jx[0] < jz[0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


#  FIRST TASK:
#  Write three functions that sum the numbers
#  in a given list using a for loop, a while loop,
#  and recursion.
class FirstTask():
    print("___________________________________________")
    print("First task:")
    print("___________________________________________")

    # first solution
    def SumFirstSolution(list):
        sum = 0

        for addend in list:
            sum += addend

        print("For loop:")
        print(list)
        print(sum)

    # second solution
    def SumSecondSolution(list):
        sum, addend = 0, 0

        while addend < len(list):
            sum += list[addend]
            addend += 1

        print("While loop:")
        print(list)
        print(sum)

    # third solution
    def SumRecursion(list):
        summ = lambda list:0 if(len(list) == 0) else list[0]+summ(list[1:])

        print("Recursion solution:")
        print(list)
        print(summ(list))


#  SECOND TASK:
#  Write a function that concatenates two lists
#  by alternating elements. For example, given
#  the two lists [a, b, c] and [1, 2, 3], the function
#  should return [a, 1, b, 2, c, 3].
def SecondTask(firstList, secondList):
    print("___________________________________________")
    print("Second Task:")
    print("___________________________________________")

    list = []
    length = max(len(firstList), len(secondList))
    index = 0

    while index < length:
        list.append(firstList[index])
        list.append(secondList[index])
        index += 1

    print(firstList)
    print(secondList)
    print(list)


#  THIRD TASK:
#  Write a function that calculates the first 100
#  Fibonacci numbers. By definition, the first two numbers
#  in the Fibonacci sequence are 0 and 1, and each
#  subsequent number is the sum of the previous two.
#  As an example, here are the first 10 Fibonacci
#  numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21 and 34.
def ThirdTask(limit):
    print("___________________________________________")
    print("Third Task:")
    print("___________________________________________")

    a, b = 0, 1
    list = []

    for index in range(limit):
        list.append(a)
        a, b = b, a + b

    print(list)


#  FOURTH TASK:
#  Write a function that takes a list of non-negative
#  integers and orders them so that they are as large
#  as possible. For example, [50, 2, 1, 9], the largest
#  generated number is 95021.
def FourthTask(list):
    print("___________________________________________")
    print("Fourth Task:")
    print("___________________________________________")
    print(list)

    arr = BubbleSortByFirstDigit(list)
    result = ""

    for index in arr:
        result += str(index)

    print(arr)
    print(int(result))


#  FIFTH TASK:
#  Write a program that puts +, -, or a space in
#  between 1, 2, ..., 9 (in that order) so that the
#  result is 100. For example:
#    1 + 2 + 34 - 5 + 67 - 8 + 9 = 100.
def FifthTask():
    pass


# main function
def main():
    FirstTask.SumFirstSolution(numbers)
    FirstTask.SumSecondSolution(numbers)
    FirstTask.SumRecursion(numbers)
    SecondTask(numbers_two, letters)
    ThirdTask(10)
    FourthTask(numbers)


# init main function
if __name__ == "__main__":
    main()
