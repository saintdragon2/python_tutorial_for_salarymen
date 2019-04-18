def wage_calculator(work_start, work_finish, wage_per_hour=7530):
    worked_hours = work_finish - work_start
    if worked_hours >= 4:
        break_time = worked_hours // 4 * 0.5
        worked_hours = worked_hours - break_time

    wage = worked_hours * wage_per_hour
    return wage, worked_hours


print('만두가게 임금계산하는 프로그램')
employee_list = ['추미애', '홍준표', '안철수', '유승민', '심상정']
work_start_list = [10, 9, 8, 9, 8]
work_finish_list = [13, 18, 17, 13, 14]


f = open('mandoo_wage.txt', 'w', encoding='utf-8')
for i in range(0, len(employee_list)):
    wage_of_the_day, worked = wage_calculator(work_start_list[i], work_finish_list[i])
    f.write('{}님은 오늘 {}시간 근무했습니다. 일당은 {}원입니다.\n'.format(
        employee_list[i], worked, wage_of_the_day
    ))

print('이 사이에 코드가 10,000줄 있다고 가정합시다. ')

f.close()


csv_file = open('csv_test_file.csv', 'w')
csv_file.write('이름, 출근시간, 퇴근시간, 근무시간, 일당\n')
for i in range(0, len(employee_list)):
    worked = work_finish_list[i] - work_start_list[i]
    wage_of_the_day, worked = wage_calculator(work_start_list[i], work_finish_list[i])
    csv_file.write('{}, {}, {}, {}, {}\n'.format(employee_list[i], work_start_list[i], work_finish_list[i], worked, wage_of_the_day))
csv_file.close()

