//const { get } = require("express/lib/response");
let album = "";
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
    return document.getElementById("title").innerText;
}

function getAuthor(){
    return document.getElementById("author").innerText;
}

function getFeelings(){
    let feelings = "";
    let chkBox = [];
    chkBox.push(document.getElementById("type-hype"));
    chkBox.push(document.getElementById("type-fun"));
    chkBox.push(document.getElementById("type-sad"));
    chkBox.push(document.getElementById("type-calm"));
    chkBox.push(document.getElementById("type-angry"));

    for(let i = 0; i < chkBox.length; i++){
        console.log(chkBox[i].value);
        if(chkBox[i].checked){
            feelings += chkBox[i].value + ", ";
        }
    }
    console.log(feelings);
    return feelings;  
}

function getData(){
    fetch("http://localhost:105/current/").then((response) => response.json()).then(json => {
        let song = json["song"];
        let artist = json["artist"];
        let url = json["art"];
        album = json["album"];

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
        artist: getAuthor(),
        song: getTitle(),
        album: album,
        rating: rating,
        feeling: getFeelings()
    };

    console.log(bodyData);
    
    fetch("http://localhost:105/submit/", {
        method: 'POST',
        headers: {
          'Content-Type': 'text/plain',
        },
        body: JSON.stringify(bodyData),
      });
})

getData();
var interval = window.setInterval(function(){
    getData();
}, 5000)