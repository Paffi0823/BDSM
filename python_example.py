#!/usr/bin/env python3
# coding=utf-8
# -*- coding: UTF-8 -*-
from flask import Flask, request
from flask import redirect, url_for
import MySQLdb
from flask import flash
app = Flask(__name__)


@app.route('/')
def index():
    form = """
    <form method="post" action="/action" >
        名字：<input name="student_name">
        <input type="submit" value="送出">
    </form>
    """
    return form


@app.route('/action', methods=['POST'])
def action():
    # 取得輸入的學生名稱
    student_name = request.form.get("student_name")
    
    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="hj",
                           passwd="test1234",
                           db="testdb")
    
    # 欲查詢的 SQL 查詢語句
    query = "SELECT student_id,student_description FROM student WHERE student_name LIKE '{}%'".format(student_name)
    
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
   
    results = """
    <p><a href="/">Back to Query Interface</a></p>
    <form method="get" action="/curriculum" >
        學生ID：<input name="student_id">
        <input type="submit" value="送出">
    """

    # 取得並列出所有查詢結果
    for (student_id, student_description) in cursor.fetchall():
        results += """<p>{}-{}</p>""".format(student_id, student_description,)
        
    return results




from flask import redirect, flash


from flask import redirect, flash

from flask import redirect, flash

@app.route('/curriculum', methods=['GET', 'POST'])
def curriculum():
    if request.method == 'POST':
        # 從表單中獲取要操作的課程 ID 和學生 ID
        student_id = request.form.get("student_id")

        # 如果表單中有新增課程 ID，則執行新增課程的操作
        if "new_course_id" in request.form:
            new_course_id = request.form.get("new_course_id")

            # 建立資料庫連線
            conn = MySQLdb.connect(host="127.0.0.1",
                                   user="hj",
                                   passwd="test1234",
                                   db="testdb")

            # 取得課程的部門名稱和學分
            cursor = conn.cursor()
            cursor.execute("SELECT dept_name, course_credit FROM course WHERE course_id = %s", (new_course_id,))
            course_dept, course_credit = cursor.fetchone()

            # 取得學生的部門名稱
            cursor.execute("SELECT dept_name FROM student WHERE student_id = %s", (student_id,))
            student_dept = cursor.fetchone()[0]

            # 檢查課程的部門名稱是否與學生的部門名稱一致
            if course_dept != student_dept:
                flash("無法加選該課程，該課程不屬於您的系別")
                conn.close()
                return redirect('/curriculum?student_id={}'.format(student_id))

            # 取得學生目前的學分
            cursor.execute("SELECT total_credit FROM student WHERE student_id = %s", (student_id,))
            total_credit = cursor.fetchone()[0]

            # 取得課程的人數上限
            cursor.execute("SELECT max_people FROM course WHERE course_id = %s", (new_course_id,))
            max_people = cursor.fetchone()[0]

            # 檢查課程的人數是否已滿
            cursor.execute("SELECT COUNT(*) FROM curriculum WHERE course_id = %s", (new_course_id,))
            current_people = cursor.fetchone()[0]

            if current_people >= max_people:
                flash("無法加選該課程，已達到人數上限")
                conn.close()
                return redirect('/curriculum?student_id={}'.format(student_id))

            # 若加選後總學分超過 30，則阻止加選操作
            if total_credit + course_credit > 30:
                flash("無法加選該課程，超過學分上限")
                conn.close()
                return redirect('/curriculum?student_id={}'.format(student_id))

            # 新增課程到 curriculum 表中
            query = "INSERT INTO curriculum (student_id, course_id) VALUES (%s, %s)"
            cursor.execute(query, (student_id, new_course_id))
            conn.commit()

            # 更新學生的總學分
            cursor.execute("UPDATE student SET total_credit = total_credit + %s WHERE student_id = %s", (course_credit, student_id))
            conn.commit()

            # 關閉資料庫連線
            conn.close()

        # 如果表單中有要刪除的課程 ID，則執行刪除課程的操作
        elif "drop_course_id" in request.form:
            drop_course_id = request.form.get("drop_course_id")

            # 建立資料庫連線
            conn = MySQLdb.connect(host="127.0.0.1",
                                   user="hj",
                                   passwd="test1234",
                                   db="testdb")

            # 取得要刪除的課程的學分
            cursor = conn.cursor()
            cursor.execute("SELECT course_credit FROM course WHERE course_id = %s", (drop_course_id,))
            drop_course_credit = cursor.fetchone()[0]

            # 刪除 curriculum 表中符合條件的記錄
            query = "DELETE FROM curriculum WHERE student_id = %s AND course_id = %s"
            cursor.execute(query, (student_id, drop_course_id))
            conn.commit()

            # 更新學生的總學分
            cursor.execute("UPDATE student SET total_credit = total_credit - %s WHERE student_id = %s", (drop_course_credit, student_id))
            conn.commit()

            # 關閉資料庫連線
            conn.close()

        # 重新導向到 curriculum 路由，重新加載課表
        return redirect('/curriculum?student_id={}'.format(student_id))

    else:
        # 從 URL 中獲取學生 ID
        student_id = request.args.get("student_id")

        # 建立資料庫連線
        conn = MySQLdb.connect(host="127.0.0.1",
                               user="hj",
                               passwd="test1234",
                               db="testdb")

        # 欲查詢的 SQL 查詢語句，加上 JOIN 語句以獲取 course_name、course_id 和 course_tmie
        query = """
        SELECT course.course_name, course.course_id, course.course_tmie 
        FROM curriculum 
        JOIN course ON curriculum.course_id = course.course_id 
        WHERE curriculum.student_id = %s 
        ORDER BY course.course_tmie ASC
        """

        # 執行查詢
        cursor = conn.cursor()
        cursor.execute(query, (student_id,))

        results = ""

        # 取得查詢結果
        for (course_name, course_id, course_tmie) in cursor.fetchall():
            # 將每個課程 ID 右側都加上課程名稱和課程時間
            results += "<p>{} - {} - {}</p>".format(course_id, course_name, course_tmie)

        # 檢查學生的總學分是否低於 9，若是則在表單下方加上提醒
        cursor.execute("SELECT total_credit FROM student WHERE student_id = %s", (student_id,))
        total_credit = cursor.fetchone()[0]
        if total_credit < 9:
            results += "<p>學分低於 9 學分</p>"

        # 關閉資料庫連線
        conn.close()

        # 表單部分 - 新增課程和刪除課程
        form = """
        <p><a href="/">Back to Query Interface</a></p>
        <form method="post">
            <label for="new_course_id">新增課程 ID：</label>
            <input type="text" id="new_course_id" name="new_course_id">
            <input type="hidden" name="student_id" value="{}">
            <input type="submit" value="新增">
        </form>
        <form method="post">
            <label for="drop_course_id">刪除課程 ID：</label>
            <input type="text" id="drop_course_id" name="drop_course_id">
            <input type="hidden" name="student_id" value="{}">
            <input type="submit" value="刪除">
        </form>
        """.format(student_id, student_id)

        # 將表單和課程 ID 返回到網頁
        return form + results
