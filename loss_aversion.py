import random
from statistics import mean
# If True win 150
# If False lose 100


def loss_aversion_game(runs):
    # Start Value
    value = 0
    for i in range(0,runs):
        rand = random.random()
        if rand >= 0.5:
            value = value + 100
        else:
            value = value - 100
    return(value)


def montecarlo(runs):
    iterations = 10000
    negative_returns = []
    returns = []
    for i in range(1,iterations):
        x = loss_aversion_game(runs)
        returns.append(x)
        if x < 0:
            negative_returns.append(x)


    print("RUNS:{} AVGGAIN:${} MIN:${} MAX:${} NEGATIVES:{}%".format(runs,
        round(mean(returns),2),
        min(returns),
        max(returns),
        round(len(negative_returns)/iterations,2)))


# MC of playing 2, 5, 10, 100, 1000

# function for game
# MC on game runs
# Get AVG Gain, Min=Largest Loss, Max = Largest Gain

# 2
montecarlo(2)
# 5
montecarlo(5)
# 10
montecarlo(10)
# 100
montecarlo(100)
# 1000
montecarlo(1000)
# 10000
montecarlo(10000)