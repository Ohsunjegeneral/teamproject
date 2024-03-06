@app.route("/")
def index():
    db = mysql.connector.connect(host='192.168.3.154', user='root', passwd='1234', database='mydb')
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT fest_count FROM festival") 
    img_paths = [item['fest_count'] for item in cursor.fetchall()] 
    db.close()
    return render_template("index.html", img_paths=img_paths)

{% for img_path in img_paths %}
    <div class="col">
      <div class="card shadow-sm">
        <img src="{{ img_path }}" /> <!-- img의 src를 fest_count로 설정 -->
        <!-- ... -->
      </div>
    </div>
{% endfor %}
