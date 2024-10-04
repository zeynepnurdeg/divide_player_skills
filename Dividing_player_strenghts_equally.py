def divide_numbers_with_equal_skills(skill):
    skill = sorted(skill)

    tot_skill = skill[0] + skill[-1]
    chem = skill[0] * skill[-1]

    for i in range(1, len(skill) // 2):
        if tot_skill != skill[i] + skill[-(i+1)]:
            return -1
        else:
            chem += skill[i] * skill[-(i+1)]

    return chem

list_of_skills = [1,2,3,4,5,6,7,8]
print(divide_numbers_with_equal_skills(list_of_skills))