m, n = int(input()), int(input())
mathematics_pupil = {input() for _ in range(m)}
informatics_pupil = {input() for _ in range(n)}
print(len(mathematics_pupil-informatics_pupil))
