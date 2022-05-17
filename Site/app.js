function setTitle(title){
    document.getElementById("title").innerText = title;
}

function setAuthor(author){
    document.getElementById("author").innerText = author;
}

function setArt(url){
    document.getElementById("album-art").src = url;
}

function getData(){
    fetch("http://localhost:105/current/").then((response) => response.json()).then(json => {
        let song = json["song"];
        let artist = json["artist"];
        let url = json["art"];
        setTitle(song);
        setAuthor(artist);
        setArt(url);
    })
}

getData();
var interval = window.setInterval(function(){
    getData();
}, 5000)