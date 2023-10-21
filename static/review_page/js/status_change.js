async function status_success(file_system_id) {
    // call route change_status_to_success
    await fetch('change_status_to_success/' + file_system_id, {
        method: "GET",
    }).then(resp => resp.json())
        .then(res => {
            console.log(res);
        }).then(() =>
            alert("審核遞交成功！")
        ).then(() => location.reload());
};

async function status_failed(file_system_id) {
    // call route change_status_to_failed
    await fetch('change_status_to_failed/' + file_system_id, {
        method: "GET",
    }).then(resp => resp.json())
        .then(res => {
            console.log(res);
        }).then(() =>
            alert("審核遞交成功！")
        ).then(() => location.reload());
};



