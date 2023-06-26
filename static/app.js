// to get the query from the form above 
const form = document.querySelector("#form")

// To react to a submit event 
form.addEventListener("submit", function(e){
    // -To avoid everything that is by default in the form like clean the form
    // after click teh submit button 
    e.preventDefault();
    getColors();
});

function getColors(){
    // Assigning the value of the form to a variable called query
    const query = form.elements.query.value ;

    // sending the request 
    fetch("/palette", {
        method : "POST", 
        headers : {
            "Content-Type" : "application/x-www-form-urlencoded"
        },
        body : new URLSearchParams({
            query: query
        })
    })
    .then((response)=>response.json())
    .then(data => {
        const colors = data.colors;
        const container = document.querySelector(".container");
        createColorBoxes(colors, container);
    });
}

function createColorBoxes(colors, container){
    // to empty the container eny time a submint button is used 
    container.innerHTML = "";
    // This is for each palette of color 
    for(const color of colors){
        const div = document.createElement("div");
        div.classList.add("color");
        div.style.backgroundColor = color;
        div.style.width = `calc(100%/${colors.length})`;

        // To show the text color when ever you click in a div 
        div.addEventListener("click", function(){
            navigator.clipboard.writeText(color)
        });

        const span = document.createElement("span");
        span.innerText = color;
        div.appendChild(span);
        container.appendChild(div);
    }
}

