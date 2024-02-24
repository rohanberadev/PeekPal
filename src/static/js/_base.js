// for navbar
const pathname = window.location.pathname;
const activeColor = "#FFD700";

const home = document.getElementById("home");
const notifications = document.getElementById("notifications");
const peeks = document.getElementById("peeks");
const vault = document.getElementById("vault");
const friends = document.getElementById("friends");
const profile = document.getElementById("profile");

console.log(pathname);

if (pathname === '/home/') {
    home.style.color = activeColor
}
else if (pathname === '/notifications/') {
    notifications.style.color = activeColor
}
else if (pathname === '/peeks/') {
    peeks.style.color = activeColor
}
else if (pathname === '/vault/') {
    vault.style.color = activeColor
}
else if (pathname === '/friends/') {
    friends.style.color = activeColor
}
else if (pathname === '/profile/') {
    profile.style.color = activeColor
}


// for default option update
if (document.getElementById("secretForm")) {

    // for default option update
    document.getElementById("option1").addEventListener("click", () => {
        document.getElementById("option1").value = document.getElementById("secret").value;
    });

    document.getElementById("option1").addEventListener("focus", () => {
        document.getElementById("option1").value = document.getElementById("secret").value;
    });

   // for add more option input 
   document.getElementById("addMoreBtn").addEventListener("click", () => {
        if (document.getElementById("option3").style.display === "none") {
            document.getElementById("option3").style.display = "block";
            document.getElementById("cancel1").style.display = "block";
        }
        else {
            document.getElementById("option4").style.display = "block";
            document.getElementById("cancel2").style.display = "block";

            document.getElementById("addMoreBtn").disabled = true;
            document.getElementById("addMoreBtn").style.color = "gray";
            document.getElementById("addMoreBtn").style.cursor = "default";
        }
   });

   document.getElementById("cancel1").addEventListener("click", () => {
        if (document.getElementById("option4").style.display === "block") {
            document.getElementById("option4").style.display = "none";
            document.getElementById("cancel2").style.display = "none";
        }
        else {
            document.getElementById("option3").style.display = "none";
            document.getElementById("cancel1").style.display = "none";

        }
        document.getElementById("addMoreBtn").disabled = false;
        document.getElementById("addMoreBtn").style.color = "black";
   });

   document.getElementById("cancel2").addEventListener("click", () => {
       document.getElementById("option4").style.display = "none";
       document.getElementById("cancel2").style.display = "none";

       document.getElementById("addMoreBtn").disabled = false;
        document.getElementById("addMoreBtn").style.color = "black";
   });
}
