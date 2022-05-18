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
        setTitle(song);
        setAuthor(artist);
        setArt(url);
        setAuthorRankLabel(artist);
    })
}

let form = document.getElementById("form");
form.addEventListener('submit', function(e){
    let rating = document.getElementById("rating").value;

    fetch("http://localhost:105/submit/1234", {
        method: "POST",
        body: JSON.stringify({
            artist: getAuthor(),
            song: getTitle(),
            rating: rating
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        }
    }).then(function(response){
        return response.json()
    })
})

getData();
var interval = window.setInterval(function(){
    getData();
}, 5000)