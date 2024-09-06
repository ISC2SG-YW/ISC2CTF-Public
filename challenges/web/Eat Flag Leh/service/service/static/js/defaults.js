async function postRequest(destination,data,action,secure,reportError){
    let formObject = new FormData()
    secure = secure ?? true
    data = data ?? {} 
    if (data instanceof FormData){
        formObject = data
    }
    else{
        for (const [key,value] of Object.entries(data)){
            formObject.append(key,value)
        }
    }
    if (reportError){
        let response = await fetch(destination, { method: "POST", body: formObject })
        let result = await response.text()
        console.log(result)
        console.log(response.headers)
    }
    let response = await fetch(destination, { method: "POST", body: formObject })
    let result
    try{
        result = await response.json()
    }
    catch (e){
        if (reportError){
            response = await fetch(destination, { method: "POST", body: formObject })
            result = await response.text()
            return result
        }
        return ""
    }
    return action ? action(result) : result 
    
}


async function getRequest(destination,data,action,secure){
    secure = secure ?? true;
    data = data ?? {} 
    destination += "?"
    console.log(data)
    for (const [key,value] of Object.entries(data)){
        destination += `${key}=${value}&`
    }
    response = await fetch(destination, 
        { method: "GET",
        headers: {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }})
    result = await response.json()
    console.log(result)
    return action ? action(result) : result 
    
}


async function readJsonFile(filePath){
    var res = await fetch(filePath)
    var response = res.json()
    return response

}

async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function checkIntersection(listA, listB) {
    const setB = new Set(listB);
    for (let i = 0; i < listA.length; i++) {
      if (setB.has(listA[i])) {
        return true;
      }
    }
    return false;
  }