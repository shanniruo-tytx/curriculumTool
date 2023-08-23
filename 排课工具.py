def is_time_conflict(schedule, new_course):
    # 检查新课程与已有课程是否时间冲突
    for course in schedule:
        for slot in course["time_slots"]:
            for new_slot in new_course["time_slots"]:
                if slot["day"] == new_slot["day"]:
                    if slot["start_time"] <= new_slot["end_time"] and new_slot["start_time"] <= slot["end_time"]:
                        if any(week in new_slot["weeks"] for week in slot["weeks"]):
                            return True
    return False

def backtrack_all(course_list, credit_requirements, current_schedule, current_credits, category_idx):
    if category_idx == len(course_list):
        if all(credit_requirements[category] == 0 for category in credit_requirements):
            return [current_schedule]
        else:
            return []
    
    category, required_credits, courses = course_list[category_idx]
    all_solutions = []
    
    for course in courses:
        if current_credits + course["credits"] <= required_credits and not is_time_conflict(current_schedule, course):
            new_schedule = current_schedule + [course]
            new_credits = current_credits + course["credits"]
            credit_requirements[category] -= course["credits"]
            
            solutions = backtrack_all(course_list, credit_requirements, new_schedule, new_credits, category_idx + 1)
            all_solutions.extend(solutions)
            
            # 回溯
            credit_requirements[category] += course["credits"]
    
    # 跳过当前类别
    solutions = backtrack_all(course_list, credit_requirements, current_schedule, current_credits, category_idx + 1)
    all_solutions.extend(solutions)
    
    return all_solutions

def generate_all_schedules(course_list, credit_requirements):
    return backtrack_all(course_list, credit_requirements, [], 0, 0)

# 示例的课程列表格式：[(类别, 需要学分, [课程1, 课程2, ...]), ...]
# 示例的课程格式：{"name": 课程名称, "credits": 学分, "time_slots": [{"day": "周一", "weeks": [1, 2], "start_time": "10:00", "end_time": "11:30"}, ...]}

course_list = [
    ("核心课", 3, [
        {"name": "课程A", "credits": 1, "time_slots": [{"day": "周四", "weeks": list(range(11, 14)), "start_time": "14:00", "end_time": "18:00"}]},
        {"name": "课程B", "credits": 1, "time_slots": [{"day": "周三", "weeks": list(range(11, 13)), "start_time": "14:00", "end_time": "18:00"}]},
        {"name": "课程c", "credits": 1, "time_slots": [{"day": "周五", "weeks": list(range(2, 5)), "start_time": "14:00", "end_time": "18:00"}]},
        # ... 更多课程
    ]),
    ("公共课", 2, [
        {"name": "现代试验设计方法与应用", "credits": 2, "time_slots": [{"day": "周三", "weeks": list(range(2, 10)), "start_time": "13:00", "end_time": "14:30"}]},
        # ... 更多课程
    ]),
    # ... 更多类别
]

credit_requirements = {
    "公共课": 2,
    "核心课": 3,
    # ... 更多类别
}

all_schedules = generate_all_schedules(course_list, credit_requirements)
if all_schedules:
    for idx, schedule in enumerate(all_schedules, start=1):
        print(f"方案 {idx}:")
        for course in schedule:
            print(f"类别：{course['category']}，课程：{course['name']}，学分：{course['credits']}，时间：{course['time_slots']}")
        print("-" * 20)
else:
    print("未找到有效的课程安排。")
