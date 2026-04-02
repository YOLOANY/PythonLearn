scores=[85,92,78,60,45]
for i in range(0,5):
    if scores[i] >= 90:
        grade = "优秀"
    elif scores[i] >= 80:
        grade = "良好"
    elif scores[i] >= 60:
        grade = "及格"
    else:
        grade = "不及格"
    print(f"学生{i+1}: {scores[i]}分 -> {grade}")