MAX_ZNAK = 100000
MIN_ZNAK = 0
NYL = "Net chisel dlya slogeniya"
def adder(*nums):
    sum = 0
    
    for n in nums:
        sum += n
    if sum > MAX_ZNAK:
        sum = MAX_ZNAK
    elif sum < 0:
        sum = MIN_ZNAK
    elif sum == 0:
        sum = NYL
    print("Сумма чисел: ", sum)

adder( 5, -10)
adder(0, 0, 0, 0)
adder(1, 2, 0, 0, 100006)