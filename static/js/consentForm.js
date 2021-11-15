function addToLocalStorage(elm) {
    let name = elm.name, id = elm.id;
    localStorage.setItem(location.href, JSON.stringify({...JSON.parse(localStorage.getItem(location.href)), [name]: id}));
}

function setInitialValues() {
    let LocalStorage = JSON.parse(localStorage.getItem(location.href));
    if(LocalStorage == null)
        return ;
    let entries = Object.entries(LocalStorage);
    for(let [k, v] of entries)
        document.getElementById(v).checked = true;
}

function redirectTo(path) {
    if(path == "/exp/demographics")
    localStorage.setItem("exp_index", 0);
    else
    localStorage.setItem("desc_index", 0);
    let form = document.getElementById("consentForm");
    form.action = path;
    form.submit();
}

window.onload = setInitialValues;