// key public actou
// key = "AIzaSyCQnghJSvTkupqj9vMbs6SdESD50lQYDEk"
// key publi pere upc
key = "AIzaSyALGc0xIGZ21GzLPx8evJ8vy8inE61uKZk"

// elrubius
// idcanal = "UCXazgXDIYyWH-yXLAkcrFxw"
// mio
idcanal = "UCzvqiTA_OIQC3y33XFl3aYA"
maxresults = "3"

busqueda = "https://youtube.googleapis.com/youtube/v3/channels?part=statistics&id="+idcanal+"&key="+key
fetch(busqueda)
.then((resposta)=>{
    return resposta.json()
    
}).then((data)=>{
    container = document.querySelector(".canal")
    container.innerHTML += `
            <h3> Suscriptors: ${data.items[0].statistics.subscriberCount} </h3>
            <h3> Videos publicats: ${data.items[0].statistics.videoCount} </h3>
            <h3> Visualitzacions: ${data.items[0].statistics.viewCount} </h3>

        `
})

busqueda = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelId="+idcanal+"&maxResults="+maxresults+"&order=date&key="+key
fetch(busqueda)
.then((resposta)=>{
    return resposta.json()
}).then((data)=>{
    let videos = data.items
    container = document.querySelector(".videos")
    for (video of videos){
        container.innerHTML += `
            <h2> ${video.snippet.title} </h2>
            <iframe width="650" height="360" align="center" src="https://www.youtube.com/embed/${video.id.videoId}" title="${video.snippet.title}" allowfullscreen></iframe>
            <h3> publicat a data: ${video.snippet.publishTime} </h3>
        `
    }
})