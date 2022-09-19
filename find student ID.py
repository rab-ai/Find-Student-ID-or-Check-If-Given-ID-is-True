number = str(input())
in_index_ = number.find("?")

if in_index_ == -1:
    number = number.split("-")
    student_number = int(number[0])
    if number[1] == "X":
        check_digit = 10
    else:
        check_digit = int(number[1])
    
    d = student_number % 10
    student_number = student_number // 10
    c = student_number % 10
    student_number = student_number // 10
    b = student_number % 10
    student_number = student_number // 10
    a = student_number
    
    calculation = a*2 + b*3 + c*5 + d*7
    
    c_check = calculation % 11
    
    if check_digit == c_check:
        print("VALID")
    else:
        print("INVALID")

if in_index_ == 5:
    number = number.split("-")
    student_number = int(number[0])
    
    d = student_number % 10
    student_number = student_number // 10
    c = student_number % 10
    student_number = student_number // 10
    b = student_number % 10
    student_number = student_number // 10
    a = student_number
    
    calculation = a*2 + b*3 + c*5 + d*7
    
    check_digit = str(calculation % 11)
    
    if check_digit == "10":
        check_digit = "X"
    
    number[1] = number[1].replace("?", check_digit)
    
    number = "-".join(number)
	
    print(number)
	
if in_index_ == 3:
    number = number.split("-")
	
    n = number[0].replace("?", "0")
    student_number = int(n)
    if number[1] == "X":
        check_digit = 10
    else:
        check_digit = int(number[1])
    
    student_number = student_number // 10
    c = student_number % 10
    student_number = student_number // 10
    b = student_number % 10
    student_number = student_number // 10
    a = student_number
    
    calculation = a*2 + b*3 + c*5
    mod = calculation % 11
    
    x = str((((check_digit - mod) % 11)*(8 % 11)) % 11)
    if check_digit == "10":
        check_digit = "X"
    number[0] = number[0].replace("?", x)
    
    number = "-".join(number)
	
    print(number)

if in_index_ == 2:
    number = number.split("-")
    n = number[0].replace("?", "0")
	
    student_number = int(n)
        
    if number[1] == "X":
        check_digit = 10
    else:
        check_digit = int(number[1])
    
    d = student_number % 10
    student_number = student_number // 10
    c = student_number % 10
    student_number = student_number // 10
    b = student_number % 10
    student_number = student_number // 10
    a = student_number
    
    calculation = a*2 + b*3 + d*7
    mod = calculation % 11

    x = str((((check_digit - mod) % 11)*(9 % 11)) % 11)
    if check_digit == "10":
        check_digit = "X"
    number[0] = number[0].replace("?", x)

    number = "-".join(number)
	
    print(number)
	
if in_index_ == 1:
    number = number.split("-")
	
    n = number[0].replace("?", "0")
    student_number = int(n)

    if number[1] == "X":
        check_digit = 10
    else:
        check_digit = int(number[1])
	
    d = student_number % 10
    student_number = student_number // 10
    c = student_number % 10
    student_number = student_number // 10
    b = student_number % 10
    student_number = student_number // 10
    a = student_number
    
    calculation = a*2 + c*5 + d*7
    mod = calculation % 11

    x = str((((check_digit - mod) % 11)*(4 % 11)) % 11)
    if check_digit == "10":
        check_digit = "X"
    number[0] = number[0].replace("?", x)
    
    number = "-".join(number)
	
    print(number)
	
if in_index_ == 0:
    number = number.split("-")
	
    n = number[0].replace("?", "0")
    student_number = int(n)

    if number[1] == "X":
        check_digit = 10
    else:
        check_digit = int(number[1])
	
    d = student_number % 10
    student_number = student_number // 10
    c = student_number % 10
    student_number = student_number // 10
    b = student_number % 10
    student_number = student_number // 10
    a = student_number
	
    calculation = b*3 + c*5 + d*7
    mod = calculation % 11
	
    x = str((((check_digit - mod) % 11)*(6 % 11)) % 11)
    if check_digit == "10":
        check_digit = "X"
    number[0] = number[0].replace("?", x)
    
    number = "-".join(number)
    
    print(number)
    

