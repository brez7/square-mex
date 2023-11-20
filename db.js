import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.1/firebase-app.js";
import { getDatabase, set, ref } from "https://www.gstatic.com/firebasejs/9.9.1/firebase-database.js";

const firebaseConfig = {
    apiKey: "AIzaSyDxBBkjzK_OVDZGuTM3qXied6Zii2sV0qM",
    authDomain: "elpueblo-switch.firebaseapp.com",
    databaseURL: "https://elpueblo-switch-default-rtdb.firebaseio.com",
    projectId: "elpueblo-switch",
    storageBucket: "elpueblo-switch.appspot.com",
    messagingSenderId: "584570551282",
    appId: "1:584570551282:web:84aca1ae6f3b52c874096b"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);

document.getElementById("contactForm").addEventListener("submit", submitForm);

function submitForm(e) {
    e.preventDefault();
    var name = getElementVal("name");
    var emailid = getElementVal("emailid");
    var msgContent = getElementVal("msgContent");
    saveMessages(name, emailid, msgContent);
    document.getElementById("contactForm").reset();
}

function saveMessages(name, emailid, msgContent) {
    set(ref(database, 'Name' + ": " + name), {
        name: name,
        emailid: emailid,
        msgContent: msgContent,
    })
};

const getElementVal = (id) => {
    return document.getElementById(id).value;
};
