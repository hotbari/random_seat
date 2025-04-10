import random
from flask import Flask, render_template

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    # 1. 수강생 명단 입력
    student_list = [
        "수강생1",
        "수강생2",
        "수강생3"
    ]


    def create_group_html(group_num, students):
        return f"""<div class="group">
            <div class="group-title">{group_num}조 ({len(students)}명)</div>
            <div class="members">{', '.join(students)}</div>
        </div>"""


    @app.route("/")
    def index():
        shuffled = student_list[:]
        random.shuffle(shuffled)
        groups_html = ""

        # 2. 한 그룹당 인원수 입력
        students_per_group = 8
        total = 0
        for i in range(10):
            start = i * students_per_group
            end = start + students_per_group
            group = shuffled[start:end]
            if not group:
                break
            total += len(group)
            groups_html += create_group_html(i + 1, group)

        return render_template('index.html', group_html=groups_html, total_students=total)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, use_reloader=True, extra_files=['templates/index.html', 'static/styles.css'])


# 3. flask run 실행