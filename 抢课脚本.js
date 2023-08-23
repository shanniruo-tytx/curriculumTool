// 定义一个函数，用于检查是否出现抢课成功的提示
function checkSuccessMessage() {
    const successMessage = document.getElementById("success-message"); // 替换为实际的成功提示元素ID或选择器
    return successMessage !== null;
}

// 定义一个函数，用于不断尝试抢课
function attemptGrabCourse() {
    const grabButton = document.getElementById("grab-course-button"); // 替换为实际的抢课按钮ID或选择器
    if (grabButton) {
        grabButton.click(); // 模拟点击抢课按钮
        
        // 检查是否出现抢课成功的提示
        if (checkSuccessMessage()) {
            console.log("抢课成功！");
        } else {
            console.log("尝试抢课中...");
            setTimeout(attemptGrabCourse, 1000); // 1秒后继续尝试抢课
        }
    } else {
        console.log("未找到抢课按钮。");
    }
}

// 开始尝试抢课
attemptGrabCourse();
