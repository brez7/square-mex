import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("react-form-ecfbb-firebase-adminsdk-g4dj5-f0d1e4b0ad.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact_form():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Save the data to Firestore
        contact_ref = db.collection("contacts").add({
            "name": name,
            "email": email,
            "message": message
        })

        return "Thank you for your message!"

    return render_template("contact_form.html")

if __name__ == "__main__":
    app.run(debug=True)
