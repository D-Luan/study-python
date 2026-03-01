import random

class Student:
    def __init__(self, id, income, score):
        self.id = id
        self.income = income
        self.score = score

    def __str__(self):
        return f"Id: {self.id}, Income: {self.income}, Score: {self.score}"

def generate_mock(quantity=10000):
    students = []
    for i in range(quantity):
        income = random.randint(0, 20000)
        if income > 10000:
            income_class = "High Income"
            score = random.uniform(200, 1000)
        elif income > 3000:
            income_class = "Medium Income"
            score = random.uniform(200, 1000)
        else:
            income_class = "Low Income"
            score = random.uniform(200, 1000)
        
        students.append(Student(i + 1, income_class, round(score, 2)))
    return students

def classify(score):
    if score < 600: return "200-599"
    elif score < 700: return "600-699"
    elif score < 800: return "700-799"
    elif score < 900: return "800-899"
    elif score <= 1000: return "900-1000"
    else: return None

def calculate_percentage(students):
    datasets = {
        '200-599': {
            "total_scores_count": 0,
            "High Income": 0,
            "Medium Income": 0,
            "Low Income": 0,
            "percentage_high_income": 0,
            "percentage_medium_income": 0,
            "percentage_low_income": 0
        },
        '600-699': {
            "total_scores_count": 0,
            "High Income": 0,
            "Medium Income": 0,
            "Low Income": 0,
            "percentage_high_income": 0,
            "percentage_medium_income": 0,
            "percentage_low_income": 0
        },
        '700-799': {
            "total_scores_count": 0,
            "High Income": 0,
            "Medium Income": 0,
            "Low Income": 0,
            "percentage_high_income": 0,
            "percentage_medium_income": 0,
            "percentage_low_income": 0
        },
        '800-899': {
            "total_scores_count": 0,
            "High Income": 0,
            "Medium Income": 0,
            "Low Income": 0,
            "percentage_high_income": 0,
            "percentage_medium_income": 0,
            "percentage_low_income": 0
        },
        '900-1000': {
            "total_scores_count": 0,
            "High Income": 0,
            "Medium Income": 0,
            "Low Income": 0,
            "percentage_high_income": 0,
            "percentage_medium_income": 0,
            "percentage_low_income": 0
        }
    }

    for student in students:
        category_key = classify(student.score)

        datasets[category_key]["total_scores_count"] += 1
        datasets[category_key][student.income] += 1

    for dataset in datasets.values():
        if not dataset["total_scores_count"] > 0:
            continue

        dataset["percentage_high_income"] = round((dataset["High Income"] / dataset["total_scores_count"]) * 100, 1)
        dataset["percentage_medium_income"] = round((dataset["Medium Income"] / dataset["total_scores_count"]) * 100, 1)
        dataset["percentage_low_income"] = round((dataset["Low Income"] / dataset["total_scores_count"]) * 100, 1)        

        if dataset["percentage_high_income"] == 0:
            dataset["percentage_high_income"] = None
        if dataset["percentage_medium_income"] == 0:
            dataset["percentage_medium_income"] = None
        if dataset["percentage_low_income"] == 0:
            dataset["percentage_low_income"] = None

    return datasets

students = generate_mock()
datasets = calculate_percentage(students)

for key, dataset in datasets.items():
    print({key})
    print(dataset)
    print("\n")