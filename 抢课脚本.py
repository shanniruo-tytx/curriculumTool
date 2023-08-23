import requests

def grab_course(session):
    # 修改为抢课页面的URL
    url = "https://your-school.edu/selectCourse"
    
    # 修改为实际的课程编号和学期
    payload = {
        "courseId": "12345",
        "semester": "2023-01"
    }

    response = session.post(url, data=payload)
    return response

# 创建一个会话
with requests.Session() as session:
    # 修改为登录操作，获取登录后的session信息
    # session.post("https://your-school.edu/login", data={"username": "your_username", "password": "your_password"})

    # 抢课
    response = grab_course(session)

    if response.status_code == 200:
        if "抢课成功" in response.text:
            print("抢课成功！")
        else:
            print("抢课失败。")
    else:
        print(f"请求失败，状态码：{response.status_code}")
