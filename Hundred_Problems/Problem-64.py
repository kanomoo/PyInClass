# grade planning for semester courses

def calculate_required_grades(current_gpa: float, target_gpa: float, credits: list[int]) -> list[str]:
    # 3.2 = (2.8 + 3.6) / 2
    # k = (2.8 + 3.6) / 2
    n = (3.2 * 2) - 2.8
    k = (2.8 + n) / 2

    return k
current_gpa = 2.8
target_gpa = 3.2
credits = [3,4,3,2,3]
print(calculate_required_grades(current_gpa, target_gpa, credits))