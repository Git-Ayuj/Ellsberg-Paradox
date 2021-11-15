let expOrder = ["/", "/exp/demographics", "/exp/sampling", "/exp/allocate", "/exp/outcome"];
let descOrder = ["/", "/desc/demographics", "/desc/allocate", "/desc/outcome"];

function checkPrevSession() {
    let pathname = new URL(location.href).pathname;
    if(pathname == "/resume" || pathname == "/invalid")
        return ;

    let currindex = expOrder.findIndex((x) => x == pathname);
    let index = localStorage.getItem("exp_index");
    if(currindex != -1 && index) {
        if(index > currindex) {
            //console.log("redirect 1!!!");
            location.href = "/resume";
        }
        else
            localStorage.setItem("exp_index", currindex);
    }
    
    currindex = descOrder.findIndex((x) => x == pathname);
    index = localStorage.getItem("desc_index");
    if(currindex != -1 && index) {
        if(index > currindex) {
            //console.log("redirect 2!!!");
            location.href = "/resume";
        }
        else
            localStorage.setItem("desc_index", currindex);
    }
}

function setSessionId(key, sid) {
    localStorage.setItem(key, sid);
}

function clearLocalStorage() {
    localStorage.removeItem("http://127.0.0.1:5000/exp/allocate");
    localStorage.removeItem("http://127.0.0.1:5000/desc/allocate");
    localStorage.removeItem("exp_index");
    localStorage.removeItem("exp_sid");
    localStorage.removeItem("desc_index");
    localStorage.removeItem("desc_sid");
}

checkPrevSession();