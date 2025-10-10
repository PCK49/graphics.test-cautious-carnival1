#app.py
#catios.py
###from flask import Flask, request, redirect, render_template_string
'''
app=Flask(__name__)

ninersite="https://49ers.com"

TEMPLATE="""
<!DOCTYPE html>
<html>
  <body>
    <p>only secret get this...</p>
    <form action="/submit" method="post">
    <input type="text" name="name" placeholder="keyword">
    <input type="submit" value="submit">
    </form>
    </body>
</html>"""

@app.route("/")
def homeforniner():
  return render_template_string(TEMPLATE)
@app.route("/submit",methods=["POST"])
def submit():
    return redirect(ninersite)
if __name__ == "__main__":
  app.run(debug=True)
'''
