//const { get } = require("express/lib/response");

function setTitle(title){
    document.getElementById("title").innerText = title;
}

function setAuthor(author){
    document.getElementById("author").innerText = author;
}

function setArt(url){
    document.getElementById("album-art").src = url;
}

function setAuthorRankLabel(author){
    document.getElementById("author-rank-label").innerText = "Was this a plus or minus for " + author;
}

function getTitle(){
    return document.getElementById("title").value;
}

function getAuthor(){
    return document.getElementById("author").value;
}

function getData(){
    fetch("http://localhost:105/current/").then((response) => response.json()).then(json => {
        let song = json["song"];
        let artist = json["artist"];
        let url = json["art"];

        if(getAuthor() != artist && getTitle() != song){
            setTitle(song);
            setAuthor(artist);
            setArt(url);
            setAuthorRankLabel(artist);
        }
    })
}

let form = document.getElementById("form");
//form.addEventListener('submit', )
form.addEventListener('submit', function(e){
    e.preventDefault();
    let rating = document.getElementById("rating").value;
    let bodyData = {
        artist: "Joe",
        song: "Poopy",
        rating: 3
    };

    // bodyData = JSON.stringify(bodyData);
    // bodyData = bodyData.trim();
    
    fetch("http://localhost:105/submit/", {
        method: "POST",
        // headers: {
        //     'Accept': 'application/json',
        //     'Content-Type': 'application/json'
        // },
        // body: JSON.stringify({
        //     artist: getAuthor(),
        //     song: getTitle(),
        //     rating: rating
        // }
        mode: 'cors',
        cache: 'default',
        body: JSON.stringify(bodyData)
        
    }).then((response) => {
        console.log("fuck");
        return response.json();
    }).then((data) => {
        console.log("Success:", data);
    }).catch((error) => {
        console.error("Error:", error);
    });
})

getData();
var interval = window.setInterval(function(){
    getData();
}, 5000)