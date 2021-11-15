function handleChange() {
    let prog1 = document.getElementById("prog1");
    let prog2 = document.getElementById("prog2");
    let value = prog1.value;
    prog2.value = 100 - Number(prog1.value);
    localStorage.setItem(location.href, JSON.stringify({...JSON.parse(localStorage.getItem(location.href)), "prog1": value}));
    localStorage.setItem(location.href, JSON.stringify({...JSON.parse(localStorage.getItem(location.href)), "prog2": 100-value}));
}

function addToLocalStorage(elm) {
    let name = elm.name, id = elm.id;
    localStorage.setItem(location.href, JSON.stringify({...JSON.parse(localStorage.getItem(location.href)), [name]: id}));
}

function setInitialValues() {
    let LocalStorage = JSON.parse(localStorage.getItem(location.href));
    if(LocalStorage == null)
        return ;
    let entries = Object.entries(LocalStorage);
    for(let [k, v] of entries) {
        if(k == "preference")
            document.getElementById(v).checked = true;
        else
            document.getElementById(k).value = v;
    }
}

window.onload = setInitialValues;