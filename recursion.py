 def factorial(n):
                        try:
                                if n == 1:
                                        return 1
                                else:
                                        return n * factorial(n-1)
                        except ValueError:
                                print("Oops!")
                                result = factorial(n)
                                print(result)
                again = input("Would you like to go again? Y or N: ").upper()
                if again == "N":
                        print("Goodbye!")
                        break

