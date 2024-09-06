const showEle = document.querySelector(".show")

const lookUpPrice = {
    "0":"Include Unlabelled Data",
    "1":"<5$",
    "2":"5 - 10$",
    "3":"10 - 20$",
    "4":">20$",
}

async function getData(){
    data = await getRequest("static/restaurants.json")
    for (var item of data){
        if (item['title'] == "Flag Part 4"){
            // phew luckily i removed the flag here!
            item['description'] = "This is the flag. You can't eat it."
        }
    }
    return data
}

async function filter(data){
    if (data == null) data = await getData()
    console.log(touse,data)
    var filtered = data.filter((item)=>{

        return checkIntersection(JSON.parse(item["cuisineType"]),touse["type"])
        && touse["price"].includes(lookUpPrice[item["price"]])
        && !touse["remove"].includes(item["title"] + " (" + item["mall"] + ")")
        && touse["malls"].includes(item["mall"])
    })
    return filtered
}

async function randomise(data){
    console.log(data)
    var randomIndex = Math.floor(Math.random() * data.length)
    return data[randomIndex]
}
async function clearData(removeContent){
    removeContent = removeContent??true
    var nameEle = document.querySelector(".restaurant-name>span")
    var imgEle = document.querySelector(".restaurant-img")
    var descEle = document.querySelector(".restaurant-desc")
    var priceEle = document.querySelector(".restaurant-price>span")
    var typeEle = document.querySelector(".restaurant-type>span")
    var mallEle = document.querySelector(".restaurant-mall>span")
    var infoDiv = document.querySelector(".restaurant-info")
    infoDiv.dataset.reverse = true
    void infoDiv.offsetWidth; // trigger a DOM reflow
    //i want to reverse an css animation then trigger it, how?
    //https://stackoverflow.com/questions/3485365/how-can-i-force-webkit-to-redraw-repaint-to-propagate-style-changes
    infoDiv.style.display = "none"
    
    if (removeContent){
        nameEle.innerText = ""
        imgEle.src = ""
        descEle.innerText = ""
        priceEle.innerText = ""
        typeEle.innerText = ""
        mallEle.innerText = ""
    }

}
async function errorMessage(){
    var errorEle = document.querySelector(".error")
    errorEle.style.display = "block"
    setTimeout(function(){
        errorEle.style.display = "none"
    }, 5000)
}
function displayData(data){
    if (!data){
        errorMessage()
        return}
    var nameEle = document.querySelector(".restaurant-name>span")
    var imgEle = document.querySelector(".restaurant-img")
    var descEle = document.querySelector(".restaurant-desc")
    var priceEle = document.querySelector(".restaurant-price>span")
    var typeEle = document.querySelector(".restaurant-type>span")
    var mallEle = document.querySelector(".restaurant-mall>span")
    var infoDiv = document.querySelector(".restaurant-info")
    var visitBtn = document.querySelector(".visit")
    var visitWebBtn = document.querySelector(".web")
    infoDiv.dataset.reverse = false
    infoDiv.style.display = "grid"

    nameEle.innerText = `${data["title"]} (${data["storeNumber"]})`
    imgEle.src = JSON.parse(data["img"])[0]    
    
    configureDesc(data["description"])
    if (data["price"] == "0"){
        priceEle.innerText = "Unlabelled"
    }
    else{
        priceEle.innerText = lookUpPrice[data["price"]]
    }
    var cuisineTypes = JSON.parse(data["cuisineType"])
    if (cuisineTypes.includes("Include Unlabelled Data")){
        typeEle.innerText = "Unlabelled"
    }
    else{
        typeEle.innerText = cuisineTypes.join(", ")
    }
    mallEle.innerText = data["mall"]
    visitBtn.onclick = function(){
        window.open(data["directoryLink"])
    }
    visitWebBtn.onclick = function(){
        window.open(data["websiteLink"])
    }
}

function configureDesc(text){
    var descEle = document.querySelector(".restaurant-desc")
    descEle.dataset.show = false
    descEle.innerText = text
    if (descEle.scrollHeight > descEle.clientHeight){
        showEle.style.display = "block"
    }else{
        showEle.style.display = "none"
    }
}

showEle.onclick = function(){
    var descEle = document.querySelector(".restaurant-desc")
    if (descEle.dataset.show == "true"){
        descEle.dataset.show = false
    }
    else{
        descEle.dataset.show = true
    }
}

