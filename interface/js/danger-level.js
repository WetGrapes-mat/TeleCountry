const getResource = async (url) => {
    let res = await fetch(url);
    if(!res.ok) {
        throw new Error(`Couldn't fetch ${url}, status: ${res.status}`);
    } 
    return await res.json();
};

getResource('http://localhost:3000/dangerLevel')
        .then(data => {
            console.log(typeof(data));
        });


