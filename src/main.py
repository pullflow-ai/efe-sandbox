def main():
    """Prints 'Hello, World!' to the console."""
    print("Hello, World!")
# Global variable with unclear name
x = []

# Function that does multiple unrelated things with poor naming
def do_stuff(a,b,c,d):   # No spaces after commas
    global x
    
    try:
        result=a+b/c*d    # No spaces around operators
    except:    # Bare except clause - bad practice
        print('error')
        return
    
    # Nested loops with unclear purpose
    for i in range(len(x)):   # Using range(len()) instead of enumerate
        for j in range(len(x[i])):
            for k in range(len(x[i][j])):
                if x[i][j][k]==result:   # No spaces around comparison operator
                    x[i][j][k]=None
                    break

# Inconsistent naming conventions
class dataProcessor:    # Class name should be CamelCase
    def __init__(self):
        self.Data = []    # Inconsistent capitalization
        
    def Process_data(self):    # Method name should be snake_case
        l = []    # Single-letter variable name
        for item in self.Data:
            if type(item)==str:    # Using type() instead of isinstance()
                l.append(int(item))    # Potential ValueError not handled
        return l

# Magic numbers with no explanation
if __name__=="__main__":
    dp=dataProcessor()
    dp.Data = ['1', '2', 'three', '4', '5']    # Mixed data types without validation
    dp.Process_data()    # Not storing or using the return value
    
    # Unnecessary list comprehension making code harder to read
    nums = [num for num in [n for n in range(100) if n % 2 == 0] if num % 3 == 0]
if __name__ == "__main__":
    main()
