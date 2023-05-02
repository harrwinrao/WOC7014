import random
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def lunch_randomiser(request):
    options = ["Nasi Lemak", "Pizza", "Burger", "Roti Canai", "Curry Mee", "Fried Rice"]
    roll = random.randint(1, 6)
    lunch_choice = options[roll - 1]
    return HttpResponse("You should have " + lunch_choice + " for lunch today!")


def display_patterns(request):
    output = ''
    for i in range(1, 8):
        output += '#'*i + '\n'
        if i == 4:
            output += '#'*i + '\n'
    output += '##\n##\n'
    return HttpResponse(output)


def marks_calculator_view(request):
    subjects = [("Biology", 5, random.randint(0, 100)), ("Mathematics", 4, random.randint(0, 100)),
                ("Chemistry", 5, random.randint(0, 100)), ("Physics", 5, random.randint(0, 100)),
                ("English", 4, random.randint(0, 100))]
    scores = []
    for subject in subjects:
        score = {
            "subject": subject[0],
            "credit_hour": subject[1],
            "mark": subject[2],
            "grade_point": get_grade_point(subject[2])
        }
        scores.append(score)
    context = {
        "scores": scores,
        "cgpa": calculate_cgp(scores)
    }
    return render(request, "markscalculator.html", context)


def calculate_cgp(scores):
    total_credit_hour = 0
    total_grade_point = 0

    for score in scores:
        credit_hour = score['credit_hour']
        total_credit_hour += credit_hour
        grade_point = get_grade_point(score['mark'])
        total_grade_point += grade_point * credit_hour

    cgp = round((total_grade_point / total_credit_hour), 2)
    return cgp


def get_grade_point(mark):
    if mark >= 80:
        return 4.0
    elif mark >= 75:
        return 3.7
    elif mark >= 70:
        return 3.3
    elif mark >= 65:
        return 3.0
    elif mark >= 60:
        return 2.7
    elif mark >= 55:
        return 2.3
    elif mark >= 50:
        return 2.0
    elif mark >= 45:
        return 1.7
    elif mark >= 40:
        return 1.3
    else:
        return 0.0

