function addToLocalStorage(elm) {
    let id = elm.id, value = elm.value;
    localStorage.setItem(location.href, JSON.stringify({...JSON.parse(localStorage.getItem(location.href)), [id]: value}));
}

function setInitialValues() {
    let LocalStorage = JSON.parse(localStorage.getItem(location.href));
    if(LocalStorage == null)
        return ;
    let entries = Object.entries(LocalStorage);
    for(let [k, v] of entries)
        document.getElementById(k).value = v;
}

window.onload = setInitialValues;
