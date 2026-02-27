# functions of probability, conditional probability and bayes theorem
def probability(favorable, total):
    return favorable / total

def conditional_probability(event_a, event_b, total):
    event_a_given_b = (event_a/total) / (event_b/total)
    return event_a_given_b

def bayes(p_b, p_a, p_a_given_b):
    p_b_given_a = (p_a_given_b * p_b) / p_a
    return p_b_given_a

# input of probability
# example 1
coin_toss_total = int(input("total number of tosses: "))
coin_toss_favorable = int(input(f"number of heads or tails in {coin_toss_total} tosses: "))

# example 2
dice_roll_favorable = 1
dice_roll_total = 6

# input of conditional probability
total_students = 100
Engineers = 60
Engineers_knows_python = 30

# input of bayes
p_disease = 0.01
p_positive_given_disease = 0.99
p_positive = 0.02

# Output of probability
# ex-1
coin_toss_probability = probability(coin_toss_favorable, coin_toss_total)
print(f"The probability of getting {coin_toss_favorable} heads or tails in {coin_toss_total} tosses is {coin_toss_probability}")

# ex-2
dice_roll_probability = probability(dice_roll_favorable, dice_roll_total)
print(dice_roll_probability)

# Output of conditional probability
prob_of_event_a_given_b = conditional_probability(Engineers_knows_python, Engineers, total_students)
print(prob_of_event_a_given_b)

# Output of bayes theorem
print(bayes(p_disease, p_positive, p_positive_given_disease))