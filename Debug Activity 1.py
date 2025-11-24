#Debug Activity 1

start
    Declarations
        num firstTest
        num secondTest
        num average
        num PASSING = 60
    output "Enter first score or 0 to quit "
    firstTest = input("Enter first score or 0 to quit")
    while firstTest <> to 0
        output "Enter second score "
        input secondTest
        average = (firstTest + secondTest) / 2
        ouput "Average is ", average
        if average >= PASSING then
            output "Pass"
        else
            output "Fail"
        endif
        output "Enter first score or 0 to quit "
    endwhile
stop


#Debug Activity 2

start
    Declarations
        string name
        num hours
        num rate
        num DEDUCTION = 45
        string EOFNAME = "ZZZ"
        num gross
        num net
    output "Enter first name or ", EOFNAME, " to quit"
    input name
    if name not equal to EOFNAME
        output "Enter hours worked for ", name
        input hours
        output "Enter hourly rate for ", name
        input rate
        gross = hours * rate
        net = gross - DEDUCTION
        if net > 0 then
            output "Net pay for ", name, " is ", net
        else
            output "Deductions not covered. Net is 0."
        endif
        output "Enter next name or ", EOFNAME, " to quit"
        input name
    endif
    output "End of job"
stop


#Debug Activity 3

start
    Declarations
        num firstTest
        num secondTest
        num average
        num PASSING = 60
    output "Enter first score or 0 to quit "
    firstTest = input("Enter first score or 0 to quit")
    while firstTest <> to 0
        output "Enter second score "
        input secondTest
        average = (firstTest + secondTest) / 2
        ouput "Average is ", average
        if average >= PASSING then
            output "Pass"
        else
            output "Fail"
        endif
        output "Enter first score or 0 to quit "
    endwhile
stop


#Debug Activity 4

start
    Declarations
        num mortgagePayment
        num utilities
        num taxes
        num upkeep
        num total
    startup()
    while mortgagePayment <> to 0
        mainLoop()
    endwhile
    finishUp()
stop

startUp()
    output "Enter your mortgage payment or 0 to quit"
    input mortgagePayment
return

mainLoop()
    output "Enter utilities"
    input utilities
    output "Enter taxes"
    input taxes
    output "Enter amount for upkeep"
    input upkeep
    total = mortgagePayment + utilities + taxes + upkeep
    output "Total is ", total
return

finishUp()
    output "End of program"
return
