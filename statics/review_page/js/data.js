async function test() {
    await fetch('get-data', {
        method: "GET",
        headers: headers,
    }).then(resp => resp.json())
        .then(res => {
            console.log(res);
        })
}

test();

