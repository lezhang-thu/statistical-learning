x = [[3, 3, 1], [4, 3, 1], [1, 1, -1]]

coef = []
for _ in range(3):
    coef.append([0, 0, 0])
#print(coef)

for i in range(3):
    for j in range(3):
        t = 0
        for k in range(2):
            t += x[i][k] * x[j][k]
        t *= 0.5
        if i >= j:
            coef[i][j] += t * x[i][2] * x[j][2]
        else:
            coef[j][i] += t * x[i][2] * x[j][2]
#print(coef)

f13 = -x[0][2] / x[2][2]
f23 = -x[1][2] / x[2][2]

for i in range(3):
    if i < 2:
        coef[i][0] += f13 * coef[2][i]
        if i >= 1:
            coef[i][1] += f23 * coef[2][i]
        else:
            coef[1][i] += f23 * coef[2][i]
    else:
        coef[0][0] += f13 * f13 * coef[2][2]
        coef[1][1] += f23 * f23 * coef[2][2]
        coef[1][0] += 2 * f13 * f23 * coef[2][2]
final = [0] * 5
final[0] = coef[0][0]
final[1] = coef[1][1]
final[2] = coef[1][0]

final[3] = -1 - f13
final[4] = -1 - f23

print(
    "{} * alpha_1^2 + {} * alpha_2^2 + {} * alpha_1 * alpha_2 + {} * alpha_1 + {} * alpha_2"
    .format(final[0], final[1], final[2], final[3], final[4]))
