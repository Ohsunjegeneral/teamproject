python
@app.route("/")
def index():
    db = mysql.connector.connect(host='192.168.3.154', user='root', passwd='1234', database='mydb')
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT fest_count FROM festival") 
    img_paths = cursor.fetchall()
    db.close()
    return render_template("index.html", count=len(img_paths), img_paths=img_paths) # count와 img_paths를 템플릿에 전달

html
{% for i in range(count) %}
    <div class="col">
      <div class="card shadow-sm">
        <img src="{{ img_paths[i]['fest_count'] }}" /> <!-- img의 src를 fest_count로 설정 -->
        <!-- ... -->
      </div>
    </div>
{% endfor %}
