async function postRequest(destination,data){
    let formObject = new FormData()
    data = data ?? {} 
    if (data instanceof FormData) formObject = data
    else{ 
        for (const [key,value] of Object.entries(data)){
            formObject.append(key,value)
        }
    }
    let response = await fetch(destination, { method: "POST", body: formObject })
    let result
    try{
        result = await response.json()
    }
    catch (e){
        alert(e)
        return "Failure"
    }
    return result 
    
}


async function report(url, ele){
    const res = await postRequest("/report", {url:url})
    console.log(res)
    if (res.error){
        alert(res.error)
        return
    }
    else{
        ele.innerText = "Reported!"
        setTimeout(() => {
            ele.innerText = "Report"
        }, 2000);
    }
}