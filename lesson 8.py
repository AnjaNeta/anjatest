"""викторина: пол-ль вводит ответ. можно дать три неверных ответа(сделать три ошибки),
после чего игра прекращается"""

answer = input("Enter your answer : ")
real = input("the right answer is ")
point =[]
# def result_count():
#     global real
#     real: "result"

def viktorina (answer, real):
    while answer == real:
        print("you get a point")
    else:
        print("please try again")
    continue


    # elif sec_ans !=real:
    #     print("please try again")
    # elif last_ans != real:
    #     print("it was your last chance")