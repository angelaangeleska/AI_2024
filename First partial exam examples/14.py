from constraint import *


def constraint_func(simona, marija, petar, meeting):
    simona_free = [13, 14, 16, 19]
    marija_free = [14, 15, 18]
    petar_free = [12, 13, 16, 17, 18, 19]

    if meeting not in simona_free or simona == 0:
        return False
    if meeting not in marija_free and marija == 1:
        return False
    if meeting not in petar_free and petar == 1:
        return False

    return petar or marija


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    meeting_domain = list(range(12, 20))

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", meeting_domain)

    variables = ['Simona_prisustvo', 'Marija_prisustvo', 'Petar_prisustvo', 'vreme_sostanok']
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(constraint_func, variables)

    # ----------------------------------------------------

    # [print(solution) for solution in problem.getSolutions()]
    for solution in problem.getSolutions():
        res = {"Simona_prisustvo": solution["Simona_prisustvo"],
               "Marija_prisustvo": solution["Marija_prisustvo"],
               "Petar_prisustvo": solution["Petar_prisustvo"],
               "vreme_sostanok": solution["vreme_sostanok"]}
        print(res)
