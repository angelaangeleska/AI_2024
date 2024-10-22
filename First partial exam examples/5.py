from constraint import *


def check_valid_all(t1, t2):
    day1, hour1 = t1.split("_")
    hour1 = int(hour1)

    day2, hour2 = t2.split("_")
    hour2 = int(hour2)

    if day1 == day2 and abs(hour1 - hour2) < 2:
        return False
    return True


def check_valid_ml(t1, t2):
    hour1 = t1.split("_")[1]
    hour2 = t2.split("_")[1]
    hour1 = int(hour1)
    hour2 = int(hour2)

    if hour1 == hour2:
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    # promenliva ke bide se ona za koe sakame da najdeme nekakva vrednost koja sto ke bide del od optimalnoto resenie
    all_variables = list()
    ml_variables = list()

    # AI predavanja
    for i in range(int(casovi_AI)):
        problem.addVariable(f'AI_cas_{i+1}', AI_predavanja_domain)
        all_variables.append(f'AI_cas_{i+1}')

    # ML predavanja
    for i in range(int(casovi_ML)):
        problem.addVariable(f'ML_cas_{i + 1}', ML_predavanja_domain)
        all_variables.append(f'ML_cas_{i + 1}')
        ml_variables.append(f'ML_cas_{i + 1}')

    # R predavanja
    for i in range(int(casovi_R)):
        problem.addVariable(f'R_cas_{i + 1}', R_predavanja_domain)
        all_variables.append(f'R_cas_{i + 1}')

    # BI predavanja
    for i in range(int(casovi_BI)):
        problem.addVariable(f'BI_cas_{i + 1}', BI_predavanja_domain)
        all_variables.append(f'BI_cas_{i + 1}')

    # AI vezbi
    problem.addVariable('AI_vezbi', AI_vezbi_domain)
    all_variables.append("AI_vezbi")

    # ML vezbi
    problem.addVariable('ML_vezbi', ML_vezbi_domain)
    all_variables.append("ML_vezbi")
    ml_variables.append("ML_vezbi")

    # BI vezbi
    problem.addVariable('BI_vezbi', BI_vezbi_domain)
    all_variables.append("BI_vezbi")

    # ---Tuka dodadete gi ogranichuvanjata----------------
    for i in range(len(all_variables)):
        for j in range(i+1, len(all_variables)):
            problem.addConstraint(check_valid_all, [all_variables[i], all_variables[j]])

    for i in range(len(ml_variables)):
        for j in range(i + 1, len(ml_variables)):
            problem.addConstraint(check_valid_ml, [ml_variables[i], ml_variables[j]])

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)