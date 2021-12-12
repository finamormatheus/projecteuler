"""
Project Euler
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
    
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
    
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

# Calculating proper divisors
function divisors(n)
    divList = Int64[1]
    
    for i in 2:√n
        if n%i == 0
            if i != n/i
                append!(divList, i)
                append!(divList, n/i)
            else
                append!(divList, i)
            end
        end
    end 

    return divList
end

# Calculate if the number is abundant
function isAbundant(n)
    divList = divisors(n)

    if sum(divList) ≤ n
        return false
    else
        return true
    end
end

# ============================================================

# Main Program 

@time begin
    # List with all abundant numbers less then 28123
    abundantList = Int64[]
    for num in 12:28123
        if isAbundant(num)
            append!(abundantList, num)
        end
    end

    # All numbers list with trues in all entries
    allNumbers = trues(28123)

    # Calculating the sums of two abundant numbers and changing the allNumbers correspondent entry to false
    for i = 1:length(abundantList)
        for j = i:length(abundantList)
            if abundantList[i] + abundantList[j] ≤ 28123
                allNumbers[abundantList[i] + abundantList[j]] = false
            else
                break
            end
        end
    end

    # Summing all true entries (all numbers that cannot be written as the sum of two abundant numbers)
    sumAllNumbers = 0
    for num in 1:28123
        if allNumbers[num]
            global sumAllNumbers += num
        end
    end

    println(sumAllNumbers)
end