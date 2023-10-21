document.addEventListener("DOMContentLoaded", function () {
    fetch('https://rag-hackthon-1.onrender.com/demo-job')
        .then(response => response.json())
        .then(


            data => {

                console.log(response)

                const tableBody = document.querySelector('tbody');

                data.forEach(row => {
                    const newRow = document.createElement('tr');
                    newRow.innerHTML = `
            <td>${row.user_id}</td>
            <td>${row.file_name}</td>
            <td>${row.question_professor}</td>
            <td>${row.question_course}</td>
            <td>${row.question_exam_type}</td>
            <td>NULL</td>
            <td>
            <a href="#" class="btn btn-success" style="margin-bottom:10px">
                <p class="success_status">Success</p>
            </a>
            <a href="#" class="btn btn-failed">
                <p class="failed_status">Failed</p>
            </a>
            </td>
          `;
                    tableBody.appendChild(newRow);
                });
            })
        .catch(error => {
            console.error('Error fetching data:', error);
        })
})





window.addEventListener("DOMContentLoaded", (event) => {
    let success_status = document.querySelector("#success_status")

    success_status.addEventListener("click", function () {
        success_status.textContent = "success";
    });
});

