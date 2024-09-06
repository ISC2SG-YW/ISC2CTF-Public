var popupContents = document.querySelectorAll(".select_options>*")
const popup = document.querySelector(".select_options")
const contentsDiv = document.querySelector(".contents")
const filterOptions = document.querySelectorAll(".filter_options")
const filterMall = document.querySelector(".filter_mall")
const filterType = document.querySelector(".filter_type")
const filterPrice = document.querySelector(".filter_price")
const filterRestaurant = document.querySelector(".filter_restaurant")
const randomiseBtn = document.querySelector(".randomise")
const removeBtn = document.querySelector(".remove")
const defaults = {
    "malls":["Jurong Point"],
    "type":[
        "Chinese",
        "Western",
        "Japanese",
        "Korean",
        "Indian",
        "Thai",
        "Malay",
        "Vietnamese",
        "Indonesian",
        "Fast Food",
        "Others",
    ],
    "price": [
    "<5$",
    "5 - 10$",
    "10 - 20$",
    ">20$"],
    "remove":[]
}
var curData = null
var curType = ""
var touse = {}
var data
function selected(newVal){
    if (newVal == "true" || newVal == "false") this.dataset.selected = newVal
    else if (this.dataset.selected == "true"){
        this.dataset.selected = false
        document.querySelector(".tick_all").dataset.selected = false
    }
    else this.dataset.selected = true
    if (this.dataset.selected == "true") touse[curType].push(this.innerText)
    else {
        idx = touse[curType].indexOf(this.innerText)
        while (idx != -1) {
            touse[curType].splice(idx,1)
            idx = touse[curType].indexOf(this.innerText)
        }
    }
    console.log(touse[curType])
    save()
}

function filterClick(){
    popup.style.display = "initial"
    contentsDiv.dataset.darken = true
}
function addToPopup(contents,type,func,tickAllText){
    popup.dataset.inverse = false
    curType = type
    var tickAll = document.createElement("div")
    tickAll.classList.add("select_option","tick_all")
    tickAll.innerText = tickAllText??`Select all ${type}`
    tickAll.onclick = function(){
        popupContents = document.querySelectorAll(".select_options>*:not(.tick_all)")
        if (this.dataset.selected == "true"){
            this.dataset.selected = "false"
        }
        else{
            this.dataset.selected = "true"
        }
        for (var ele of popupContents){
            // console.log(this.dataset.selected,this)
            ele.onclick(this.dataset.selected)
        }
        
    }
    popup.appendChild(tickAll)
    var reference = touse[type]
    var allTicked = true
    console.log(contents)
    for (var content of contents){
        if (func) content = func(content)
        const newOption = document.createElement("div")
        newOption.classList.add("select_option")
        newOption.innerText = content
        newOption.dataset.selected = false
        newOption.onclick = selected
        popup.appendChild(newOption)
        if (reference.includes(content)){
            newOption.dataset.selected = true
        }
        else allTicked = false
    }
    if (allTicked) tickAll.dataset.selected = true
}
console.log("ran")
contentsDiv.onclick = function(e){
    console.log(e.target)
    if (e.target.classList.contains("report_btn")) return
    if (e.target.classList.contains("filter_options")) return
    this.dataset.darken = false 
    popup.style.display = "none"
}

for (var ele of popupContents){
    ele.onclick = selected
}




function loadSaved(){
    var saved = localStorage.getItem("saved")
    if (saved){
        touse = JSON.parse(saved)
    }
    else{
        touse = defaults
    }
}

function save(){
    localStorage.setItem("saved",JSON.stringify(touse))
}
function initialise(){
    loadSaved()
    getData()
}

initialise()



filterMall.onclick = function(){
    filterClick()
    // q: how to remove elements in the popup
    popup.textContent = ""
    const malls = [
        "Jurong Point",
        "JEM",
        "Westgate",
        "JCube",
        "IMM Building",
        "Jewel Changi Airport",
        "Bedok Mall",
        "Junction 8",
        "Funan",
        "Plaza Singapura",
        "Bugis+ (Part of Bugis Town)",
        "Bugis Junction (Part of Bugis Town)",
        "Tampines Mall",
        "Bukit Panjang Plaza",
        "Lot One Shoppers' Mall",
        "Raffles City Shopping Centre",
        "Clarke Quay",
        "Sengkang Grand Mall"
    ]
    addToPopup(malls,"malls",null,"Select all Malls")
}

filterType.onclick = function(){
    filterClick()
    popup.textContent = ""
    const types = [
        "Include Unlabelled Data",
        "Chinese",
        "Western",
        "European",
        "Mexican",
        "Japanese",
        "Korean",
        "Indian",
        "Thai",
        "Malay",
        "Vietnamese",
        "Indonesian",
        "Cafe/Beverages",
        "Dessert",
        "Fast Food",
        "Bakery",
        "Others",
    ]
    addToPopup(types,"type",null,"Select all Food Types",true)
}

filterPrice.onclick = function(){
    filterClick()
    popup.textContent = ""
    const prices = [
        "Include Unlabelled Data",
        "<5$",
        "5 - 10$",
        "10 - 20$",
        ">20$",
    ]
    addToPopup(prices,"price",null,"Select all Price Ranges")
}

randomiseBtn.onclick = async function(){
    var res = await filter(data)
    var random = await randomise(res)
    curData = random
    displayData(random)
}

filterRestaurant.onclick = async function(){
    filterClick()
    popup.textContent = ""
    addToPopup(await filter(data),"remove",(res)=>res["title"] + " (" + res["mall"] + ")", "Add all Restaurants")
    var tickAll = document.querySelector(".tick_all")
    tickAll.dataset.selected = false
    tickAll.onclick = function(){
        popupContents = document.querySelectorAll(".select_options>*:not(.tick_all)")
        for (var ele of popupContents){
            console.log(ele)
            ele.onclick("false")
        }
    }
    popup.dataset.inverse = true
}

removeBtn.onclick = function(){
    if (curData && !touse["remove"].includes(curData["title"])) touse["remove"].push(curData["title"] + " (" + curData["mall"] + ")")
    clearData()
    curData = null
    save()
}
function flagPart3(str, shift) {
    if (shift < 0) return flagPart3(str, shift + 26);
    let result = '';
    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        if (char.match(/[a-z]/i)) {
            const code = str.charCodeAt(i);
            if (code >= 65 && code <= 90) {
                result += String.fromCharCode(((code - 65 + shift) % 26) + 65);
            } else if (code >= 97 && code <= 122) {
                result += String.fromCharCode(((code - 97 + shift) % 26) + 97);
            }
        } else {
            result += char;
        }
    }
}

flagPart3("_Mw_CYQ",-4)
// I request that you do not request the request


