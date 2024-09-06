const polluteButton = document.getElementById("pollute");
function processCookies(cookies) {
  const cookieObject = {};
  cookies.split(";").forEach((cookie) => {
    const [key, value] = cookie.split("=");
    cookieObject[key.trim()] = value;
  });
  return cookieObject;
}
polluteButton.addEventListener("click", () => {
  const cookies = processCookies(document.cookie);
  const uuid = cookies["uuid"];
  const token = cookies["token"];
  var amount = 1;
  const formData = new URLSearchParams();
  formData.append("uuid", uuid);
  formData.append("token", token);
  formData.append("amount", amount);
  fetch("/pollute", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: formData.toString(),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data['success']){
        polluteButton.innerHTML = "Polluted!";
        polluteButton.disabled = true;
      }
      else{
        alert(data['error']);
      }
    });
});
