def SketchStudent(*args, Status=False):
    '''
    '''

    notas = {"Total": len(args),
             "Highestscore": max(args),
             "Lowestscore": min(args),
             "Media": sum(args) / len(args)}

    if Status:
        if notas['Media'] >= 8:
            notas['Status'] = "VERY GOOD"

        elif notas['Media'] >= 5:
            notas['Status'] = "ACCEPTABLE"

        else:
            notas['Status'] = "BAD"

    return notas


izi = SketchStudent(4, 5, 5, Status=True)
print(izi)
